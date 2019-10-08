import socket

all_connections = []
all_address = []

global host
global port
global s

host = "192.168.2.2"
port = 9000

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

num1 = conn.recv(1024).decode()
num2 = conn.recv(1024).decode()
print("Valores recebido do cliente -> " + "Num1: " + str(num1) + " Num2: " + str(num2))

print("Enviando dados para o participante 1...")
ipParticipante1 = '192.168.2.2'
socketParticipante1 = socket.socket()
socketParticipante1.connect((ipParticipante1, 9001))
dados = str(num1) + ';' + str(num2)
socketParticipante1.send(dados.encode())
respotaParticipante1 = socketParticipante1.recv(1024).decode()
print("Valores recebido do participante1 -> " + str(respotaParticipante1))
conn.send(respotaParticipante1.encode())



