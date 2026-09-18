-- Simplified Control4 DriverWorks-style mock driver. Illustrative only.
-- Not runnable outside Composer Pro.

function DriverInit()
    C4:UpdateProperty("Driver Status", "Offline")
    C4:UpdateProperty("Power State", "Off")
    C4:SetTimer(1000, "PollDevice")
end

function PollDevice()
    local ip = C4:GetProperty("Device IP")
    if ip == "" then
        C4:UpdateProperty("Driver Status", "Offline")
        C4:Log("ERROR", "No IP configured")
        return
    end
    -- Real driver: open TCP socket, send STATUS, parse response.
    C4:UpdateProperty("Driver Status", "Online")
    C4:Log("INFO", "Device reachable at " .. ip)
end

function OnPropertyChanged(property)
    if property == "Power" then
        local state = C4:GetProperty("Power")
        C4:SendToDevice("POWER_" .. string.upper(state))
        C4:UpdateProperty("Power State", state)
        C4:Log("INFO", "Power set to " .. state)
    end
end

function DriverDestroy()
    C4:Log("INFO", "Driver destroyed")
end