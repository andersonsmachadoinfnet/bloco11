import socket
import ssl

HOST = "127.0.0.1"
PORT = 8443

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    context.load_verify_locations(cafile="cert.pem")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = context.wrap_socket(s, server_hostname=HOST)
    s.close()

    client.connect((HOST, PORT))
    print('Cliente: Conexão estabelecida ')

    message = input(" Digite algo ou tchau para finalizar-> ")  

    while message.lower().strip() != 'tchau':
        client.send(message.encode())  # enviando mensagem
        data = client.recv(1024).decode()  # recebendo resposta

        print('Cliente: Recebido: ' + data)

        message = input(" Digite algo ou tchau para finalizar-> ")