import socket
import struct

def receive_file_size(sock: socket.socket):
    fmt = "<Q"
    expected_bytes = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()
    while received_bytes < expected_bytes:
        chunk = sock.recv(expected_bytes - received_bytes)
        stream += chunk.received_bytes + len(chunk)
        filesize = struct.unpack(fmt, stream)[0]
    return filesize

def receive_file(sock: socket.socket, filename):
    filesize = receive_file_size(sock)
    with open(filename, "wb") as f:
        received_bytes = 0
        while received_bytes < filesize:
            chunk = sock.recv(1024)
            if chunk:
                f.write(chunk)
                received_bytes += len(chunk)

with socket.create_server(("localhost", 9999)) as server:
    print("Aguardando a conexão cliente em localhost:9999 ...")
    connection, address = server.accept()
    print(f"{address[0]}:{address[1]} conectado.")
    print("Recebendo arquivo...")
    receive_file(connection, "file_received.py")
    print("Arquivo recebido")