LPAREN = string.byte("(")
OR     = string.byte("=")
AND    = string.byte("+")

function test_logic(s)
    local tok = ""
    local lhs = 0
    local rhs = -1

    if s:byte() == LPAREN then
        tok = s:match("^%b()")

        local inner = tok:sub(2, #tok-1)

        lhs = test_logic(inner)
    else
        tok = s:match("^[%w_{}]+")

        if tok:sub(1, 2) == "e_" then
            -- This is an event
            local event = "@Events/"..tok
            local section = Tracker:FindObjectForCode(event)

            if section.AccessibilityLevel == AccessibilityLevel.Normal then
                lhs = 1
            end
        else
            -- This is an inventory item or an option
            local item = tok
            local required = 1

            -- Flag and Titania_Piece will have counts
            local count_s = tok:match("%b{}")
            if count_s then
                required = tonumber(count_s:sub(2, #count_s - 1))

                item = item:sub(1, #item - #count_s)
            end

            local found = Tracker:ProviderCountForCode(item)
            if found >= required then
                lhs = 1
            end
        end
    end

    if s == tok then
        return lhs
    end

    -- If tok wasn't the full string, the remainder will be an operator followed by the other operand
    local rest = s:sub(#tok + 1)
    local op = rest:byte()

    -- Short-circuit
    if op == OR and lhs > 0 then
        return 1
    elseif op == AND and lhs == 0 then
        return 0
    end
    
    rhs = test_logic(rest:sub(2))

    if op == OR then
        if lhs > 0 or rhs > 0 then
            return 1
        end
        return 0
    elseif op == AND then
        if lhs > 0 and rhs > 0 then
            return 1
        end
        return 0
    end
end
