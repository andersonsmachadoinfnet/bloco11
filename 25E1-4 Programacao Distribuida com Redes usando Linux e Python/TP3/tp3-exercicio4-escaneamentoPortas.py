import socket

ip = '127.0.0.1'
port_ini = int(input("Digite a porta inicial: "))
port_fim = int(input("Digite a porta final: "))
for port in range(port_ini, port_fim+1):
    print(f"Testando porta {port}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    if result==0:
        print(f"  porta {port} aberta!")
    sock.close
print("fim")
