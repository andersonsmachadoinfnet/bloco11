import subprocess
import sys

def varredura_portas(ip):
    print(f"Iniciando varredura de portas para o IP: {ip}")
    
    comando = ["nmap", "-p", "1-65535", ip]

    try:
        resultado = subprocess.check_output(comando, stderr=subprocess.STDOUT, universal_newlines=True)
        
        print(resultado)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o Nmap: {e.output}")
    except FileNotFoundError:
        print("Nmap não encontrado. Certifique-se de que o Nmap está instalado.")

ip_alvo = sys.argv[1]
varredura_portas(ip_alvo)
