import usocket as socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addre = s.accept()
    request = conn.recv(1024)
    request = str(request)
    print(request)

    response = "Hello MicroPython(Web Sever)"
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()
