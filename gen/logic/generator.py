#! /usr/bin/env python3

import csv
import pathlib

from mappings import REGIONS

LOGIC_FILE = pathlib.Path("gen") / "logic" / "RustedMossLogic.csv"
LOCATIONS_FILE = pathlib.Path("locations") / "locations.jsonc"

START_LOCATION = "rm_start_0[100390]"

GOAL_POS_GLOBAL = (2472, 3376)

LOC_TO_REGION = dict()

# TODO: Split this into sane functions.
def generate_poptracker_logic():
  transitions = dict()
  events = dict()
  checks = dict()

  with open(LOGIC_FILE) as logic_file:
    logic_csv = csv.reader(logic_file)
    init_room_to_region_map()

    for region in REGIONS:
      transitions[region] = dict()
      checks[region] = dict()

    for row in logic_csv:
      if len(row) < 3 or not is_room(row[0]):
        # Skip rows that don't have logic (i.e. the first row)
        # Rows should have 4 items each, but I don't care about notes
        continue
      loc_from = row[0]  # This is always a transition
      region_from = region_of(loc_from)  # As such it always has an associated region

      loc_to = row[1]  # Could be transition, event, or check

      loc_requires = clean_requires(row[2])

      if is_room(loc_to):
        region_to = region_of(loc_to)

        t = transitions[region_to].setdefault(loc_to, dict())
        t[loc_from] = loc_requires

        # The logic seems to not always define both directions for transitions, so I've added them
        # to ensure PopTracker properly connects everything.
        # This may add false positives in some spots, such as vertical shafts that cannot be traversed upwards.
        if loc_to != loc_from and not loc_requires:
          t = transitions[region_from].setdefault(loc_from, dict())
          if loc_to not in t:
            t[loc_to] = loc_requires
      elif is_event(loc_to):
        # I'm not tracking regions for events, since they don't necessarily occur where they are relevant
        e = events.setdefault(loc_to, dict())
        e[loc_from] = loc_requires
      else:  # Check
        # I *am* trackings regions for checks, since it lets me be more organized with the json
        item = clean_loc(loc_to)
        region_to = region_from
        room = clean_loc(loc_from)

        r = checks[region_to].setdefault(room, dict(items=dict()))
        if not "map" in r:
          r["map"] = REGIONS[region_to]["items"][item]["global"]
        c = r["items"].setdefault(item, dict())
        c[loc_from] = loc_requires


  # TODO: PopTracker will throw an error if locations.jsonc has more than 1k dangling commas.
  # For now, can use this find-and-replace to fix them, or prettify (but this breaks formatting in ways I don't like):
  #     ,(\n\s*)([\]\}])
  #     $1$2

  # TODO: Overall I would like to clean this up, maybe just using a JSON library or whatever.
  # TODO: Split transition and event logic into their own files
  with open(LOCATIONS_FILE, "w", encoding="utf-8") as lf:
    ind = 0
    write(lf, "[", ind)
    ind += 2
    for region in REGIONS:
      write(lf, "{", ind)

      ind += 2
      write(lf, f"\"name\": \"{region}\",", ind)

      write(lf, "\"sections\": [", ind)
      ind += 2
      for t in transitions[region]:
        write(lf, "{", ind)
        ind += 2

        write(lf, f"\"name\": \"{t}\",", ind)
        write(lf, "\"item_count\": 0,", ind)

        if t != START_LOCATION:
          write(lf, "\"access_rules\": [", ind)
          ind += 2

          for source in transitions[region][t]:
            source_region = region_of(source)
            requirement = transitions[region][t][source]
            if requirement:
              write(lf, f"\"@{source_region}/{source},$test_logic|{requirement}\",", ind)
            else:
              write(lf, f"\"@{source_region}/{source}\",", ind)

          ind -= 2
          write(lf, "],", ind)  # "access_rules"

        ind -=2
        write(lf, "},", ind)  # Transition
      ind -= 2
      write(lf, "],", ind)  # "sections"

      write(lf, "\"children\": [", ind)
      ind += 2

      for room in checks[region]:
        write(lf, "{", ind)
        ind += 2

        checks_in_room = checks[region][room]["items"]
        # TODO: I would like to have each room's sections ordered deterministically, and ideally
        # in the same order as in-game in the case of shops.
        items_in_room = list(checks_in_room)

        match len(checks_in_room):
          case 1:
            room_name = items_in_room[0]
          case 2:
            if "Flag" in items_in_room:
              # For stylistic reasons I'm naming these consistently with flag as the second item
              other_item = [i for i in items_in_room if i != "Flag"][0]
              room_name = f"{other_item} + Flag"
            else:
              room_name = "Pistol + TP UP"
          case 3:
            # Only shops have three items in a room
            room_name = f"{region} Shop"
          case n:
            print(f"Unmatched number ({n}) of checks in room '{room}'")
            exit(1)

        write(lf, f"\"name\": \"{room_name}\",", ind)
        write(lf, "\"sections\": [", ind)
        ind += 2
        for item in items_in_room:
          write(lf, "{", ind)
          ind += 2

          write(lf, f"\"name\": \"{item}\",", ind)
          write(lf, "\"item_count\": 1,", ind)
          write(lf, "\"access_rules\": [", ind)
          ind += 2

          for source in checks_in_room[item]:
            source_region = region_of(source)
            requirement = checks_in_room[item][source]
            if requirement:
              write(lf, f"\"@{source_region}/{source},$test_logic|{requirement}\",", ind)
            else:
              write(lf, f"\"@{source_region}/{source}\",", ind)

          ind -=2
          write(lf, "]", ind)  # Access Rules

          ind -= 2
          write(lf, "},", ind)  # Section

        ind -= 2
        write(lf, "],", ind)  # "sections"

        if "map" in checks[region][room]:
          write(lf, "\"map_locations\": [", ind)
          ind += 2

          # TODO: Include locations for the local maps
          write(lf, "{", ind)
          ind += 2

          pos = checks[region][room]["map"]
          write(lf, "\"map\": \"full\",", ind)
          write(lf, f"\"x\": {pos[0]},", ind)
          write(lf, f"\"y\": {pos[1]},", ind)

          ind -= 2
          write(lf, "},", ind)

          ind -= 2
          write(lf, "],", ind)  # "map_locations"

        ind -= 2
        write(lf, "},", ind)  # Child
      
      ind -= 2
      write(lf, "],", ind)  # "children"

      ind -= 2
      write(lf, "},", ind)  # Region

    write(lf, "{", ind)
    ind += 2

    write(lf, "\"name\": \"Events\",", ind)
    write(lf, "\"children\": [", ind)
    ind += 2

    for e in events:
      write(lf, "{", ind)
      ind += 2

      write(lf, f"\"name\": \"{e}\",", ind)
      write(lf, "\"access_rules\": [", ind)
      ind += 2

      for source in events[e]:
        source_region = region_of(source)
        requirement = events[e][source]
        if requirement:
          write(lf, f"\"@{source_region}/{source},$test_logic|{requirement}\",", ind)
        else:
          write(lf, f"\"@{source_region}/{source}\",", ind)

      ind -=2
      write(lf, "],", ind)  # Event access_rules

      ind -= 2
      write(lf, "},", ind)  # Event section

    ind -= 2
    write(lf, "],", ind)  # "sections"

    ind -= 2
    write(lf, "},", ind)  # Events

    # TODO: Add map markers for certain events (tea party, questlines, etc)

    write(lf, "{", ind)
    ind += 2
    
    write(lf, "\"name\": \"Goal\",", ind)
    write(lf, "\"sections\": [", ind)
    ind += 2

    for goal in "abcde":
      write(lf, "{", ind)
      ind += 2

      write(lf, f"\"name\": \"Ending {goal.upper()}\",", ind)
      write(lf, f"\"item_count\": 1,", ind)
      write(lf, "\"access_rules\": [", ind)
      ind += 2

      write(lf, f"\"@Events/e_goal_{goal}\",", ind)

      ind -=2
      write(lf, "],", ind)  # Goal access_rules

      write(lf, "\"visibility_rules\": [", ind)
      ind += 2

      write(lf, f"\"ending_{goal}\",", ind)

      ind -=2
      write(lf, "],", ind)  # Goal visibility_rules

      ind -= 2
      write(lf, "},", ind)  # Goal section

    ind -= 2
    write(lf, "],", ind)  # "sections"

    write(lf, "\"map_locations\": [", ind)
    ind += 2

    write(lf, "{", ind)
    ind += 2

    write(lf, f"\"map\": \"full\",", ind)
    write(lf, f"\"x\": {GOAL_POS_GLOBAL[0]},", ind)
    write(lf, f"\"y\": {GOAL_POS_GLOBAL[1]},", ind)
    write(lf, f"\"shape\": \"diamond\",", ind)
    write(lf, f"\"size\": 56,", ind)

    ind -= 2
    write(lf, "},", ind)  # Goal map location

    ind -= 2
    write(lf, "],", ind)  # Goal map_locations

    ind -= 2
    write(lf, "},", ind)  # Goal

    ind -= 2
    write(lf, "]", ind)


def write(lf, line, ind, nonl=False):
  lf.write(f"{" "*ind}{line}{"" if nonl else "\n"}")

def init_room_to_region_map():
  for region in REGIONS:
    for room in REGIONS[region]["rooms"]:
      LOC_TO_REGION[room] = region

def clean_loc(loc: str) -> str:
  if is_room(loc):
    brace = loc.find("[")
    return loc[:brace] if brace >= 0 else loc
  if is_event(loc):
    return loc

  # If it's not a room or an event, it's an item, which means the location starts with its region name.
  for region in REGIONS:
    if loc.startswith(region):
      return loc[len(region) + 1:]

  # Already clean? Just return it.
  return loc

def clean_requires(req: str) -> str:
  # Remove spaces for ease of parsing, and change | to = because | is a special character in location rules
  return req.replace(" ", "").replace("|", "=")

def region_of(loc: str) -> str:
  cleaned = clean_loc(loc)

  if cleaned not in LOC_TO_REGION:
    print(f"Location '{cleaned}' ({loc}) not in room-to-region map")
    exit(1)
  return LOC_TO_REGION[cleaned]

def is_room(loc: str) -> bool:  # Or transition
  return loc.startswith("rm_") or loc.startswith("rfae_")

def is_event(loc: str) -> bool:
  return loc.startswith("e_")


if __name__ == "__main__":
  generate_poptracker_logic()
