from scapy.all import ARP, Ether, srp

# Definindo o intervalo de IP
target_ip = "192.168.1.0/24"

# Criando o pacote ARP e encapsulando em Ethernet
arp_request = ARP(pdst=target_ip)
broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
arp_request_broadcast = broadcast/arp_request

# Enviando o pacote e recebendo as respostas
answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

# Exibindo as respostas
print("IP Address\t\tMAC Address")
print("-----------------------------------------")
for element in answered_list:
    print(f"{element[1].psrc}\t\t{element[1].hwsrc}")
