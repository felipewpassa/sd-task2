import socket

all_connections = []
all_address = []

global host
global port
global s

host = "192.168.2.2"
port = 9001

s = socket.socket()
s.bind((host, port))
s.listen(1)

auxQuantMaquinas = 1
print("Aguardando conexões...")

while auxQuantMaquinas:
    conn, address = s.accept()
    all_connections.append(conn)
    all_address.append(address)
    print("Conexão estabelecida: " + address[0])
    auxQuantMaquinas = auxQuantMaquinas - 1

dados = conn.recv(1024).decode()
dados = dados.split(';')
num1 = dados[0]
num2 = dados[1]
print("Dados recebido do coordenador -> Num1: " + num1 + " Num2: " + num2)
resultado = float(num1) + float(num2)
print("Enviando resultado da soma para o coordenador")
conn.send(str(resultado).encode())