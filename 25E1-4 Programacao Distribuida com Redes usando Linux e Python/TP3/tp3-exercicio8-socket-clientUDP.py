import socket
SERVER_IP = "127.0.0.1"
SERVER_PORT = 6789
address = (SERVER_IP ,SERVER_PORT)
socket_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    message = input("Entre com a sua mensagem > ")
    if message=="tchau":
        break
    socket_client.sendto(bytes(message,encoding='utf8'),address)
    response_server,addr = socket_client.recvfrom(4096)
    print("Resposta do servidor => %s" % response_server.decode())
    socket_client.close()