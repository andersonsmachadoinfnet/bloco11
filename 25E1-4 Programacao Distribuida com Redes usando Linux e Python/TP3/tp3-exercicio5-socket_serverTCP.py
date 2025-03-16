import socket


def server_program():
    host = socket.gethostname()
    port = 5000  # Inicializando na porta 5000

    server_socket = socket.socket()  # obtendo a instância
    server_socket.bind((host, port))  # vinculando endereco e porta

    # Definindo 2 clientes a serem ouvidos simultaneamente
    server_socket.listen(2)
    conn, address = server_socket.accept()  # aceitou conexao
    print("Conexao de: " + str(address))
    while True:
        # Recebendo dados em pacote de ate 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Dado recebido: " + str(data))
        data = input(' Responder-> ')
        conn.send(data.encode())  # Envia resposta

    conn.close()  # fecha conexao


if __name__ == '__main__':
    server_program()