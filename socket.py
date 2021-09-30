import socket

sock = socket.socket(socket.socket.SOCK_STREAM)
sock.connect(("us1.ghash.io",3333))

sock.send("""{"id": 1, "method": "mining.subscribe","params": []}\n""")
print (sock.recv(4000))

sock.send("""{"params": ["kens_1", "password"], "id":2, "method": "mining.authorize"}\n""")
print (sock.recv(4000))
