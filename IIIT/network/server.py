import socket

s = socket.socket()
print("Socket created successfully")

# reserve a port on your computer in our case it is 12345

port = 12345

# TODO: bind to the port
# we have not types any ip  in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network

s.bind(("", port))
print("Socket binded to %s", (port))

s.listen(5)
print("Socket is listing")

while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send("Thank you for connecting".encode())

    c.close()
    break
