search_term = 'Giuseppe Vizzari'
port = 50003
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", port))

sock.send(search_term)

res = []
while True:
  c = self._sock.recv(1)
  if c == "\n":
    return "".join(res)
  res.append(c)

print res

port2 = 50004
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", port2))
sock.send(search_term)

res = []
while True:
  c = self._sock.recv(1)
  if c == "\n":
    return "".join(res)
  res.append(c)

print res
