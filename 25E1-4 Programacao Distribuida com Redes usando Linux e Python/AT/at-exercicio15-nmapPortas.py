import nmap

nm = nmap.PortScanner()

alvo = input('Digite o ip de varredura: ')

portas = '1-10000'

print(f"Iniciando a varredura nas portas {portas} da rede {alvo}...")
nm.scan(hosts=alvo, arguments=f'-p {portas}')

for host in nm.all_hosts():
    print(f'\nHost: {host}')
    print('Estado:', nm[host].state())
    print('Portas abertas:')
    
    for proto in nm[host].all_protocols():
        print(f' Protocolo: {proto}')
        lport = nm[host][proto].keys()
        for port in lport:
            print(f'  Porta: {port} - Estado: {nm[host][proto][port]["state"]}')
