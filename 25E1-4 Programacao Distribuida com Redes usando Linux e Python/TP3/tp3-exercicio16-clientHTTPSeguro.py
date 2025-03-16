import ssl
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_socket = ssl.SSLSocket(sock)
data = bytearray()
try:
    secure_socket.connect(("localhost", 4443))
    print(secure_socket.cipher())
    secure_socket.write(b"GET / HTTP/1.1 \r\n")
    secure_socket.write(b"Host: localhost\n\n")
    data = secure_socket.read()
    print(data.decode("utf-8"))
except Exception as exception:
    print("Exception: ", exception)