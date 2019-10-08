import socket

ipCoordenador = '192.168.2.2'
arrayDados = []

s1 = socket.socket()
s1.connect((ipCoordenador, 9000))

print("Conectado! Pronto para receber dados...")

num1 = input("Digite o digito 1: ")
num2 = input("Digite o digito 2: ")

s1.send(num1.encode())
s1.send(num2.encode())

respostaCoordenadorP1 = s1.recv(1024).decode()
print("Dados recebido do coordenado P1 -> " + str(respostaCoordenadorP1))

concorda = input("Concorda com o dado: S | N")

if (concorda == "S"):
    arrayDados.append(respostaCoordenadorP1)
