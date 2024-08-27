local socket = require("socket")
local client = socket.tcp()

client:connect("your_ip", 4422) -- edit 'your_ip' to match the server ip or port, lol

while true do
    io.write("> ") -- sending
    client:send(io.read("*l") .. "\n")
    print(client:receive()) -- receive
end
