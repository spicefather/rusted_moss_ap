#! /usr/bin/env python3

# TODO: Local positions for all checks

REGIONS = {
  "Flatlands": {
    "rooms": [
      "rm_4_hidden", "rm_4_hidden_2", "rm_4_hidden_3", "rm_boss_test", "rm_catacombs_alt_check", "rm_hidden_4",
      "rm_mount_shortcut", "rm_start_0", "rm_start_1", "rm_start_2", "rm_start_2_alt", "rm_start_get_ability",
      "rm_tea_intro_0", "rm_tea_party", "rm_test_2", "rm_test_3", "rm_test_3_alt", "rm_test_4", "rm_test_4_alt",
      "rm_test_4_alt_2", "rm_test_4_alt_3", "rm_test_5", "rm_test_6", "rm_test_6_shortcut", "rm_test_7",
      "rm_test_7_alt", "rm_test_7_alt_2", "rm_test_8", "rm_test_alt", "rm_test_alt_alt", "rm_test_before_boss",
      "rm_test_before_boss_alt", "rm_test_boss", "rm_test_hidden", "rm_test_hidden_2",  "rm_test_void_0",
      "rm_test_void_1", "rm_test_void_2",

      "rm_hook_tutorial_0", "rm_hook_tutorial_1", "rm_hook_tutorial_2", "rm_hook_tutorial_3", "rm_hook_tutorial_4",
      "rm_hook_tutorial_5",

      # This one should be `rm_test_hidden_3` according to the Interactive Map
      "rm_test_3_hidden", 
    ],
    "items": {
      "Flag": {"global": (2088, 912), "local": (987, 654)},
      "Grappling Hook": {"global": (2088, 1040), "local": (987, 654)},
      "HP Overload": {"global": (1768, 1168), "local": (987, 654)},
      "HP UP (Bottom)": {"global": (1832, 1296), "local": (987, 654)},
      "HP UP (Top Left)": {"global": (1768, 1104), "local": (987, 654)},
      "HP UP (Top Right)": {"global": (2280, 1104), "local": (987, 654)},
      "MP UP (Bottom Left)": {"global": (1704, 1232), "local": (987, 654)},
      "MP UP (Top Right)": {"global": (1896, 976), "local": (987, 654)},
      "Thorny Wings": {"global": (2024, 912), "local": (987, 654)},
      "Time Manipulator": {"global": (2088, 1232), "local": (987, 654)},
      "Titania Piece": {"global": (2280, 1232), "local": (987, 654)},
      "TP UP": {"global": (1896, 1040), "local": (987, 654)},
    }
  },
  "Factory Roof": {
    "rooms": [
      "rm_moss_0", "rm_moss_1", "rm_moss_2", "rm_moss_3", "rm_moss_5", "rm_moss_6", "rm_moss_7", "rm_moss_8",
      "rm_moss_8_alt", "rm_moss_chain_intro", "rm_moss_hidden_0", "rm_moss_hidden_1", "rm_moss_hidden_2",
      "rm_moss_to_sea", "rm_moss_top_0", "rm_moss_top_1", "rm_moss_top_2", "rm_moss_top_3", "rm_moss_top_4",
      "rm_moss_top_5", "rm_moss_top_6", "rm_moss_top_7", "rm_moss_top_boss", "rm_moss_top_cave", "rm_moss_top_cave_2",
      "rm_moss_top_cave_2_alt", "rm_moss_top_hidden_1", "rm_moss_top_hidden_3", "rm_moss_top_hidden_4",
      "rm_moss_top_right", "rm_moss_top_save", "rm_seer", "rm_seer_intro", "rm_seer_teleport", "rm_seer_teleport_alt",
      "rm_test", "rm_test_tunnel_right",
    ],
    "items": {
      "Charge Jump": {"global": (2984, 912), "local": (987, 654)},
      "Erosive Bullets": {"global": (2792, 1040), "local": (987, 654)},
      "Flag": {"global": (2472, 912), "local": (987, 654)},
      "Giant Chambers": {"global": (2408, 1232), "local": (987, 654)},
      "Magnet": {"global": (2408, 1232), "local": (987, 654)},
      "MP UP": {"global": (2600, 1104), "local": (987, 654)},
      "Pistol": {"global": (2344, 1168), "local": (987, 654)},
      "Spiced Gunpowder": {"global": (2408, 1232), "local": (987, 654)},
      "Thorny Rose": {"global": (2472, 912), "local": (987, 654)},
      "TP UP (Bottom Left)": {"global": (2344, 1168), "local": (987, 654)},
      "TP UP (Middle)": {"global": (2600, 1040), "local": (987, 654)},
      "TP UP (Top Right)": {"global": (2664, 848), "local": (987, 654)},
    }
  },
  "Snowy Outpost": {
    "rooms": [
      "rm_snow_0", "rm_snow_1", "rm_snow_11", "rm_snow_12", "rm_snow_13", "rm_snow_2", "rm_snow_3", "rm_snow_4",
      "rm_snow_5", "rm_snow_6", "rm_snow_7", "rm_snow_intro_0", "rm_snow_intro_1", "rm_snow_intro_2", "rm_snow_intro_3",
    ],
    "items": {
      "Energy Disruptor": {"global": (1448, 848), "local": (987, 654)},
      "Grenade": {"global": (1448, 336), "local": (987, 654)},
    }
  },
  "Smoked Forest": {
    "rooms": [
      "rm_4_hidden_to_mount", "rm_meadow_to_snow_0", "rm_meadow_to_snow_1", "rm_meadow_to_snow_2",
      "rm_meadow_to_snow_3", "rm_mount_0", "rm_mount_1", "rm_mount_10_alt_2", "rm_mount_10_alt", "rm_mount_10",
      "rm_mount_11", "rm_mount_12", "rm_mount_13", "rm_mount_2", "rm_mount_3_alt_2", "rm_mount_3_alt_hidden",
      "rm_mount_3_alt", "rm_mount_3", "rm_mount_4_half_left", "rm_mount_4_half_right", "rm_mount_4",
      "rm_mount_5_right_2", "rm_mount_5_right_3", "rm_mount_5_right", "rm_mount_5", "rm_mount_6_ext", "rm_mount_6",
      "rm_mount_7", "rm_mount_8_alt", "rm_mount_8", "rm_mount_9_right_2", "rm_mount_9_right", "rm_mount_9",
      "rm_mount_alt_1", "rm_mount_alt_2", "rm_mount_alt_4", "rm_mount_alt_begin", "rm_mount_ameli_0",
      "rm_mount_ameli_1", "rm_mount_before_boss_extra", "rm_mount_before_boss_shortcut", "rm_mount_before_boss",
      "rm_mount_begin", "rm_mount_boss", "rm_mount_elevator", "rm_mount_intro_1", "rm_mount_intro_begin",
      "rm_mount_jank_0", "rm_mount_jank_1", "rm_mount_jank_2", "rm_mount_right_1", "rm_mount_right_2",
      "rm_mount_right_3", "rm_mount_right_4", "rm_mount_right_alt_0", "rm_mount_right_alt_1", "rm_mount_right_alt_2",
      "rm_mount_top_boss", "rm_mount_top_left_1", "rm_mount_top_left_2", "rm_mount_top_left_3",
      "rm_mount_top_left_4_alt", "rm_mount_top_left_4", "rm_mount_top_left_5", "rm_mount_top_left_6",
      "rm_mount_top_left_7", "rm_mount_top_left_8_alt", "rm_mount_top_left_8", "rm_mount_top_left_boss",

      # Individual challenge rooms are not written in logic
      # "rm_ameli_c_0", "rm_ameli_c_1", "rm_ameli_c_2", "rm_ameli_c_3", "rm_ameli_c_4",
      # "rm_ameli_c_5", "rm_ameli_c_6", "rm_ameli_c_7", "rm_ameli_c_9",
    ],
    "items": {
      "Fae Silver (Bottom Left)": {"global": (1960, 784), "local": (987, 654)},
      "Fae Silver (Top Right)": {"global": (2408, 336), "local": (987, 654)},
      "Flag": {"global": (2152, 656), "local": (987, 654)},
      "HP UP": {"global": (2152, 656), "local": (987, 654)},
      "MP UP": {"global": (2536, 848), "local": (987, 654)},
      "Powdered Nightshade": {"global": (2344, 272), "local": (987, 654)},
      "Short Fuse": {"global": (1768, 528), "local": (987, 654)},
      "Sniper": {"global": (1640, 400), "local": (987, 654)},
      "Sprite's Breath": {"global": (1896, 400), "local": (987, 654)},
      "Titania Piece": {"global": (2120, 80), "local": (987, 654)},
      "Titania's Protection": {"global": (1896, 848), "local": (987, 654)},
      "TP UP": {"global": (2088, 464), "local": (987, 654)},
    }
  },
  "Mountainside": {
    "rooms": [
      "rm_sea_0", "rm_sea_1", "rm_sea_1_secret", "rm_sea_10", "rm_sea_11", "rm_sea_12", "rm_sea_2", "rm_sea_3",
      "rm_sea_4", "rm_sea_5", "rm_sea_6", "rm_sea_7_new", "rm_sea_8", "rm_sea_8_alt", "rm_sea_9",
      "rm_sea_arena_reward", "rm_sea_boss", "rm_sea_extra_0", "rm_sea_extra_1", "rm_sea_extra_2", "rm_sea_left_0",
      "rm_sea_left_1", "rm_sea_left_2", "rm_sea_mid_0", "rm_sea_mid_1", "rm_sea_mid_2_alt", "rm_sea_mid_left_0",
      "rm_sea_mid_left_1", "rm_sea_mid_right_0", "rm_sea_mid_right_1", "rm_sea_mid_save", "rm_sea_mid_setpice",
      "rm_sea_new_0", "rm_sea_new_0_alt", "rm_sea_new_1", "rm_sea_new_1_alt", "rm_sea_new_2", "rm_sea_new_2_alt",
      "rm_sea_new_3", "rm_sea_new_3_2", "rm_sea_new_3_4", "rm_sea_new_4", "rm_sea_new_5", "rm_sea_new_6",
      "rm_sea_new_save_bot_alt", "rm_sea_to_boss_0", "rm_sea_to_boss_1", "rm_sea_to_boss_2", "rm_sea_to_boss_3",
      "rm_sea_to_boss_save", "rm_sea_top_0", "rm_sea_top_1", "rm_sea_top_2", "rm_sea_top_3", "rm_sea_top_4",
      "rm_sea_top_5", "rm_sea_top_6", "rm_sea_top_7", "rm_sea_top_boss", "rm_sea_top_extra", "rm_sea_top_extra_2",
      "rm_sea_top_extra_connector",

      # Individual challenge rooms are not written in logic
      # "rm_seer_c", "rm_seer_c_0", "rm_seer_c_0_1", "rm_seer_c_1", "rm_seer_c_2", "rm_seer_c_3", "rm_seer_c_4",
      # "rm_seer_c_5", "rm_seer_c_6", "rm_seer_c_7", "rm_seer_c_final",
    ],
    "items": {
      "Energy Refiner": {"global": (2792, 1808), "local": (987, 654)},
      "Fae Silver (Bottom)": {"global": (2856, 1744), "local": (987, 654)},
      "Fae Silver (Top)": {"global": (3112, 1360), "local": (987, 654)},
      "Flag": {"global": (3048, 1872), "local": (987, 654)},
      "Guardian Fae": {"global": (3240, 720), "local": (987, 654)},
      "HP UP": {"global": (3048, 1936), "local": (987, 654)},
      "MP UP (Bottom)": {"global": (2984, 1296), "local": (987, 654)},
      "MP UP (Top)": {"global": (2984, 976), "local": (987, 654)},
      "Ruby Slippers": {"global": (3112, 1232), "local": (987, 654)},
      "Titania Piece": {"global": (2632, 1904), "local": (987, 654)},
    }
  },
  "Lab": {
    "rooms": [
      "rm_lab_0", "rm_lab_1", "rm_lab_2", "rm_lab_3", "rm_lab_4", "rm_lab_5", "rm_lab_6", "rm_lab_7",
      "rm_lab_alt_intro_0", "rm_lab_bed_0", "rm_lab_bed_1", "rm_lab_bed_2", "rm_lab_bleft_0", "rm_lab_bleft_1",
      "rm_lab_bleft_2", "rm_lab_bleft_3", "rm_lab_bleft_4", "rm_lab_bleft_5", "rm_lab_boss", "rm_lab_entry_to_save",
      "rm_lab_left_2", "rm_lab_left_3", "rm_lab_main_left_0", "rm_lab_main_left_1", "rm_lab_main_left_2",
      "rm_lab_main_left_3", "rm_lab_main_left_4", "rm_lab_main_left_5", "rm_lab_main_left_6", "rm_lab_main_left_7",
      "rm_lab_main_left_8", "rm_lab_orange_0", "rm_lab_orange_2_0", "rm_lab_orange_2_1", "rm_lab_orange_2_alt",
      "rm_lab_red_0", "rm_lab_red_1", "rm_lab_red_2", "rm_lab_red_3", "rm_lab_red_4", "rm_lab_red_5", "rm_lab_red_6",
      "rm_lab_red_7", "rm_lab_red_8", "rm_lab_red_alt", "rm_lab_save", "rm_lab_save_right_0", "rm_lab_save_right_1",
      "rm_lab_save_right_2", "rm_lab_save_right_3", "rm_lab_save_right_4", "rm_lab_save_right_5",
      "rm_lab_save_right_6", "rm_lab_to_boss_0", "rm_lab_to_boss_1", "rm_lab_to_boss_3", "rm_lab_to_boss_4",
      "rm_lab_to_boss_5", "rm_lab_to_boss_6", "rm_lab_to_boss_7", "rm_lab_to_boss_8", "rm_lab_to_cat_0",
      "rm_lab_to_cat_4", "rm_lab_to_cat_5", "rm_lab_to_cat_6", "rm_lab_to_cat_7", "rm_lab_to_cat_8", "rm_lab_to_cat_9",
      "rm_lab_upper_2", "rm_lab_upper_3", "rm_lab_upper_4", "rm_lab_upper_5", "rm_lab_upper_w_2", "rm_lab_upper_w_3",
      "rm_lab_upper_w_4", "rm_lab_upper_w_5", "rm_tea_intro_1",
    ],
    "items": {
      "Fae of Love": {"global": (776, 1328), "local": (987, 654)},
      "Fae Silver (Left)": {"global": (232, 1168), "local": (987, 654)},
      "Fae Silver (Middle)": {"global": (936, 1296), "local": (987, 654)},
      "Fae Silver (Right)": {"global": (1128, 1104), "local": (987, 654)},
      "Maya's Trinket": {"global": (40, 1168), "local": (987, 654)},
      "Rusted Coin": {"global": (104, 912), "local": (987, 654)},
      "Titania Piece": {"global": (1160, 1520), "local": (987, 654)},
    }
  },
  "Ichor Refinery": {
    "rooms": [
      "rm_catacombs_0", "rm_catacombs_0_0", "rm_catacombs_0_1", "rm_catacombs_0_2", "rm_catacombs_1",
      "rm_catacombs_1_0", "rm_catacombs_1_2", "rm_catacombs_10", "rm_catacombs_12", "rm_catacombs_13",
      "rm_catacombs_2", "rm_catacombs_2_0", "rm_catacombs_2_1", "rm_catacombs_2_2", "rm_catacombs_3", "rm_catacombs_4",
      "rm_catacombs_5", "rm_catacombs_6", "rm_catacombs_7", "rm_catacombs_8", "rm_catacombs_9",
      "rm_catacombs_alt_entry", "rm_catacombs_alt_entry_2", "rm_catacombs_alt_entry_3", "rm_catacombs_alt_secret",
      "rm_catacombs_boss", "rm_catacombs_boss_after", "rm_catacombs_extra_0", "rm_catacombs_extra_1",
      "rm_catacombs_extra_2", "rm_catacombs_extra_3", "rm_catacombs_extra_4", "rm_catacombs_extra_4_alt",
      "rm_catacombs_extra_5", "rm_catacombs_extra_lore_0", "rm_catacombs_extra_lore_1", "rm_catacombs_furnace",
      "rm_catacombs_furnace_shortcut", "rm_catacombs_furnace_storage_0", "rm_catacombs_furnace_storage_1",
      "rm_catacombs_furnace_storage_2", "rm_catacombs_furnace_top", "rm_catacombs_right_0", "rm_catacombs_right_1",
      "rm_catacombs_right_2", "rm_catacombs_right_3", "rm_catacombs_right_5", "rm_catacombs_right_6",
      "rm_catacombs_right_7", "rm_catacombs_right_8", "rm_catacombs_right_boss", "rm_catacombs_right_extra",
      "rm_catacombs_right_shortcut", "rm_catacombs_save_1", "rm_catacombs_save_1_alt", "rm_catacombs_save_2",
      "rm_catacombs_save_3", "rm_catacombs_to_moss_0", "rm_catacombs_to_moss_1", "rm_catacombs_to_moss_2",
      "rm_catacombs_to_moss_fall", "rm_catacombs_tunnel_0", "rm_catacombs_tunnel_1", "rm_catacombs_tunnel_2",
    ],
    "items": {
      "Cleansing Charm": {"global": (1320, 1424), "local": (987, 654)},
      "Fae Silver (Bottom Right)": {"global": (1512, 1488), "local": (987, 654)},
      "Fae Silver (Top Left)": {"global": (1384, 1296), "local": (987, 654)},
      "Flag": {"global": (2024, 1488), "local": (987, 654)},
      "MP UP": {"global": (1576, 1680), "local": (987, 654)},
      "Shotgun": {"global": (1896, 1680), "local": (987, 654)},
      "Tattered Blindfold": {"global": (2024, 1744), "local": (987, 654)},
      "Titania Piece": {"global": (1736, 1584), "local": (987, 654)},
      "TP UP": {"global": (1896, 1808), "local": (987, 654)},
    }
  },
  "Living Quarters": {
    "rooms": [
      "rm_forest_boss", "rm_forest_boss_after", "rm_forest_boss_after_shortcut", "rm_forest_boss_after_to_side",
      "rm_forest_branch_0_0", "rm_forest_branch_0_1", "rm_forest_branch_0_2", "rm_forest_branch_0_3",
      "rm_forest_branch_0_4", "rm_forest_branch_1_0", "rm_forest_branch_1_1", "rm_forest_branch_1_2",
      "rm_forest_branch_1_3", "rm_forest_branch_1_4", "rm_forest_branch_2_0", "rm_forest_branch_2_1",
      "rm_forest_branch_2_2", "rm_forest_branch_2_3", "rm_forest_branch_2_4", "rm_forest_branch_2_5",
      "rm_forest_branch_2_6", "rm_forest_branch_3_0", "rm_forest_branch_3_1", "rm_forest_branch_3_2",
      "rm_forest_branch_3_3", "rm_forest_branch_4_0", "rm_forest_branch_4_1", "rm_forest_branch_4_2",
      "rm_forest_branch_4_3", "rm_forest_branch_5_0", "rm_forest_branch_5_1", "rm_forest_branch_5_2",
      "rm_forest_cafe_0", "rm_forest_cafe_1", "rm_forest_cafe_2", "rm_forest_cafe_3", "rm_forest_core_0",
      "rm_forest_core_1", "rm_forest_core_2", "rm_forest_core_3", "rm_forest_core_4", "rm_forest_core_5",
      "rm_forest_core_6",  "rm_forest_extra_0", "rm_forest_extra_1", "rm_forest_extra_2", "rm_forest_extra_3",
      "rm_forest_extra_4", "rm_forest_lilly", "rm_forest_to_cata_0", "rm_forest_to_cata_1", "rm_forest_to_hell_0",
      "rm_forest_to_hell_1", "rm_forest_to_rain", "rm_forest_tutorial_0", "rm_forest_tutorial_1",
      "rm_forest_tutorial_2", "rm_forest_tutorial_3", "rm_titanias_head",

      # Individual challenge rooms are not written in logic
      # "rm_shopkeeper_c_0", "rm_shopkeeper_c_1", "rm_shopkeeper_c_2", "rm_shopkeeper_c_3_0", "rm_shopkeeper_c_3_1",
      # "rm_shopkeeper_c_4_0", "rm_shopkeeper_c_4_1", "rm_shopkeeper_c_5", "rm_shopkeeper_c_6_0", "rm_shopkeeper_c_6_1",
      # "rm_shopkeeper_c_7", "rm_shopkeeper_c_8", "rm_shopkeeper_c_9",

      # "rm_forest_dev_room",
    ],
    "items": {
      "Bolt Dispenser": {"global": (2792, 1424), "local": (987, 654)},
      "Cracked Monocle": {"global": (2152, 1872), "local": (987, 654)},
      "Fae Silver (Bottom Left)": {"global": (2600, 1680), "local": (987, 654)},
      "Fae Silver (Top Right)": {"global": (2728, 1552), "local": (987, 654)},
      "Flag": {"global": (2344, 1296), "local": (987, 654)},
      "Grappling Hook Upgrade": {"global": (2344, 2000), "local": (987, 654)},
      "HP UP": {"global": (2216, 1936), "local": (987, 654)},
      "Lucky Clover Pearl": {"global": (2152, 1424), "local": (987, 654)},
      "MP UP": {"global": (2152, 1360), "local": (987, 654)},
      "Titania Piece (Head)": {"global": (2408, 1808), "local": (987, 654)},
      "Titania Piece": {"global": (2696, 1456), "local": (987, 654)},
      "TP UP": {"global": (2280, 1808), "local": (987, 654)},
      "Wing Clipper": {"global": (2408, 1424), "local": (987, 654)},
    }
  },
  "Lake": {
    "rooms": [
      "rm_lake_0", "rm_lake_1", "rm_lake_2", "rm_lake_3", "rm_lake_4", "rm_lake_5", "rm_lake_6", "rm_lake_7",
      "rm_lake_boss", "rm_lake_boss_after_0", "rm_lake_boss_after_1", "rm_lake_boss_after_2", "rm_lake_boss_after_3",
      "rm_lake_boss_after_4", "rm_lake_core_old", "rm_lake_extra_0", "rm_lake_extra_1", "rm_lake_extra_1_alt",
      "rm_lake_extra_2", "rm_lake_extra_3", "rm_lake_extra_4", "rm_lake_extra_5", "rm_lake_extra_6",
      "rm_lake_hidden_0", "rm_lake_hidden_1", "rm_lake_hidden_2", "rm_lake_hidden_3", "rm_lake_hidden_4",
      "rm_lake_hidden_5", "rm_lake_save_0", "rm_lake_under_0", "rm_lake_under_1", "rm_lake_under_10",
      "rm_lake_under_11", "rm_lake_under_12", "rm_lake_under_14", "rm_lake_under_15", "rm_lake_under_16",
      "rm_lake_under_17", "rm_lake_under_18", "rm_lake_under_19", "rm_lake_under_2", "rm_lake_under_20",
      "rm_lake_under_21", "rm_lake_under_22", "rm_lake_under_23", "rm_lake_under_24", "rm_lake_under_25",
      "rm_lake_under_26", "rm_lake_under_27", "rm_lake_under_28", "rm_lake_under_29", "rm_lake_under_3",
      "rm_lake_under_3_alt", "rm_lake_under_4", "rm_lake_under_5", "rm_lake_under_7", "rm_lake_under_8",
      "rm_lake_under_8_alt", "rm_lake_under_9",
    ],
    "items": {
      "Dandelion Bomb": {"global": (3240, 2192), "local": (987, 654)},
      "Fae of Glass": {"global": (3240, 2192), "local": (987, 654)},
      "Fae of Hate": {"global": (3880, 1744), "local": (987, 654)},
      "Fae Silver (Left)": {"global": (3048, 2192), "local": (987, 654)},
      "Fae Silver (Right)": {"global": (3432, 2256), "local": (987, 654)},
      "Magnetic Bullets": {"global": (3240, 2192), "local": (987, 654)},
      "MP UP": {"global": (3432, 2128), "local": (987, 654)},
      "Rocket Launcher": {"global": (2984, 2192), "local": (987, 654)},
      "Titania Piece": {"global": (3400, 2352), "local": (987, 654)},
      "TP UP": {"global": (3304, 2128), "local": (987, 654)},
    }
  },
  "Pipe": {
    "rooms": [
      "rm_pipe_0", "rm_pipe_1", "rm_pipe_3", "rm_pipe_4", "rm_pipe_6", "rm_pipe_7",
    ],
    "items": {}
  },
  "Barrows Ceiling": {
    "rooms": [
      "rm_catacombs_alt_entry_tunnel", "rm_catacombs_to_hell", "rm_catacombs_to_hell_0", "rm_catacombs_to_hell_1",
      "rm_catacombs_to_hell_2", "rm_catacombs_to_hell_2_alt", "rm_catacombs_to_hell_3", "rm_catacombs_to_hell_4",
      "rm_hell_0", "rm_hell_1", "rm_hell_2", "rm_hell_3", "rm_hell_4", "rm_hell_5", "rm_hell_6", "rm_hell_garden",
      "rm_hell_garden_alt", "rm_hell_right_0", "rm_hell_right_1", "rm_hell_right_2", "rm_hell_right_2_alt",
      "rm_hell_right_3", "rm_hell_right_4", "rm_hell_right_5", "rm_hell_right_6", "rm_hell_right_7",
      "rm_hell_right_7_alt", "rm_hell_right_8", "rm_hell_to_desert", "rm_hell_to_forest", "rm_underhang_b00",
      "rm_underhang_b01", "rm_underhang_b02", "rm_underhang_b10", "rm_underhang_b11", "rm_underhang_b12",
      "rm_underhang_b13", "rm_underhang_b20", "rm_underhang_b21", "rm_underhang_b22", "rm_underhang_b23",
      "rm_underhang_b24", "rm_underhang_b30", "rm_underhang_b31", "rm_underhang_b32", "rm_underhang_b33",
      "rm_underhang_boss", "rm_underhang_boss_after", "rm_underhang_core", "rm_underhang_core_1",
      "rm_underhang_core_2", "rm_underhang_core_3", "rm_underhang_core_4", "rm_underhang_core_5",
      "rm_underhang_core_6", "rm_underhang_core_7", "rm_underhang_extra_0", "rm_underhang_extra_1",
      "rm_underhang_extra_2", "rm_underhang_extra_3_0", "rm_underhang_extra_3_1", "rm_underhang_extra_4",
      "rm_underhang_tunnel_start", "rm_underhang_tunnel_to_elfheim",
    ],
    "items": {
      "Cricket Bone Whip": {"global": (2152, 2320), "local": (987, 654)},
      "Fae Silver": {"global": (2408, 2320), "local": (987, 654)},
      "HP UP": {"global": (2344, 2704), "local": (987, 654)},
      "Incendiary Essence": {"global": (2984, 2512), "local": (987, 654)},
      "TP UP": {"global": (2280, 2256), "local": (987, 654)},
    }
  },
  "Elfame": {
    "rooms": [
      "rfae_00", "rfae_01", "rfae_02", "rfae_03", "rfae_04", "rfae_10", "rfae_11", "rfae_12", "rfae_13", "rfae_14",
      "rfae_20", "rfae_21", "rfae_22", "rfae_23", "rfae_30", "rfae_31", "rfae_32", "rfae_33", "rfae_40", "rfae_41",
      "rfae_42", "rfae_43", "rfae_50", "rfae_51", "rfae_52", "rfae_boss", "rfae_c0", "rfae_c1", "rfae_c2", "rfae_c3",
      "rfae_c4", "rfae_c5", "rfae_c52", "rfae_c6", "rfae_h0", "rfae_h1", "rfae_h2", "rfae_h4", "rfae_intro",
      "rfae_right_0", "rfae_right_1", "rfae_right_2",

      # Ending D only
      "rfae_boss_puck_pre_2", "rfae_boss_puck_pre_3", "rfae_boss_puck_pre", "rfae_boss_puck",
    ],
    "items": {
      "Fae Silver (Left)": {"global": (2152, 3152), "local": (987, 654)},
      "Fae Silver (Middle)": {"global": (2280, 3216), "local": (987, 654)},
      "Fae Silver (Right)": {"global": (2792, 3088), "local": (987, 654)},
      "Fairy Ointment": {"global": (2280, 3024), "local": (987, 654)},
      "Fern's Trinket": {"global": (2216, 2960), "local": (987, 654)},
      "Heavy Ammo": {"global": (2280, 3024), "local": (987, 654)},
      "Infinite Grapple": {"global": (2408, 3376), "local": (987, 654)},
      "Powdered Fae Silver": {"global": (2280, 3024), "local": (987, 654)},
    }
  },
}
