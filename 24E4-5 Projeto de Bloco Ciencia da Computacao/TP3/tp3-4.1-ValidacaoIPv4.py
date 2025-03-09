import ipaddress

def checaIp(ip, rede):
    encontrou = False
    for addr in ipaddress.IPv4Network(rede):
        lip = str(addr)
        if ip==lip:
            encontrou = True
    return encontrou

ip = '192.168.1.5'
rede='192.168.1.0/24'    
if checaIp(ip, rede):
    print(f'IP {ip} válido na rede {rede}')
else:
    print(f'IP {ip} inválido na rede {rede}')