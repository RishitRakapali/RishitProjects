import socket

def http_get(host, page):
    request = 'GET ' + page + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'
    sock = socket.create_connection((host, 80))
    sock.sendall(request.encode(encoding='utf-8'))
    data = sock.recv(1000)
    print(data.decode())
    sock.close()

def http_head(host,page):
    request = 'HEAD ' + page + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'
    sock = socket.create_connection((host, 80))
    sock.sendall(request.encode(encoding='utf-8'))
    data = sock.recv(1000)
    print(data.decode())
    sock.close()

http_head('50.87.178.13', '/CScourses/03b1_minimal.html')
#http_get('www.google.com', '/')