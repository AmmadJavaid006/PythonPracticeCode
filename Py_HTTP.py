import socket

handel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
handel.connect(("data.pr4e.org", 80))
cammand = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
handel.send(cammand)

while True:
    data = handel.recv(200)
    if (len(data) < 1):
        break
    print(data.decode())