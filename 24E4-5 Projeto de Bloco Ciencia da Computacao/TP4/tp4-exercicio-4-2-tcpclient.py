import socket

def client_program():
    host = socket.gethostname()  
    port = 5000  # porta 5000

    client_socket = socket.socket()  # inicializando
    client_socket.connect((host, port))  # conectando ao servidor

    message = input(" Digite algo ou tchau para finalizar-> ")  

    while message.lower().strip() != 'tchau':
        client_socket.send(message.encode())  # enviando mensagem
        data = client_socket.recv(1024).decode()  # recebendo resposta

        print('Recebido do servidor: ' + data)

        message = input(" Digite algo ou tchau para finalizar-> ")  

    client_socket.close()

if __name__ == '__main__':
    client_program()