import ssl
address = ('www.uol.com.br', 443)
certificate = ssl.get_server_certificate(address)
print(certificate)