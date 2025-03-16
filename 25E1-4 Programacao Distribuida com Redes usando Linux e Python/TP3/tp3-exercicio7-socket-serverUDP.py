import socket,sys
SERVER_IP = "127.0.0.1"
SERVER_PORT = 6789
socket_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_server.bind((SERVER_IP,SERVER_PORT))
print("[*] Servidor UDP escutando em %s:%d" % (SERVER_IP,SERVER_PORT))
while True:
    data,address = socket_server.recvfrom(4096)
    socket_server.sendto("Servidor aguardando conexões...".encode(),address)
    data = data.strip()
    print("Mensagem %s recebuda de %s: "% (data.decode(), address))
    try:
        response = "Olá %s" % sys.platform
    except Exception as e:
        response = "%s" % sys.exc_info()[0]
    print("Resposta",response)
    socket_server.sendto(bytes(response,encoding='utf8'),address)
    socket_server.close()