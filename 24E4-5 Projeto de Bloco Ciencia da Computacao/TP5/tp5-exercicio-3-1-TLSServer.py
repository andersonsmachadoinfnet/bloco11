import socket
import ssl

HOST = "127.0.0.1"
PORT = 8443

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    context.load_verify_locations(cafile="cert.pem")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = context.wrap_socket(s)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.close()

    server.bind((HOST, PORT))
    server.listen(0)

    while True:
        connection, client_address = server.accept()
        print("Conexao estabelecida com  " + str(client_address))
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Recebido: {data.decode('utf-8')}")
            data = input(' Responder-> ')
            connection.send(data.encode())  # Envia resposta