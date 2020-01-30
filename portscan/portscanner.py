import socket
import sys

#portas
number = 0
portas = []
portas.append(number) #porta 0
while not number == 65536:
    portas.append(number)
    number = number + 1


#scanner#
def scanner(dominio, tempo):
    for porta in portas:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(tempo)
        codigo = cliente.connect_ex((dominio, porta))
        if codigo == 0:
            print("Port: {} : OPEN".format(porta))

#visual
def traco():
    print("-"*50)



def main():
    traco()
    print("Welcome to the Python PortScan!\nThis script scans the 65536 existing ports.")
    traco()
    try:
        dominio = str(input("Domain/ip: "))
        tempo = float(input("Time in seconds: "))
    except:
        print("Error")
        traco()
        sys.exit()
    traco()
    #scan
    print("Scanning...")
    scanner(dominio, tempo)
    traco()


if __name__ == "__main__":
    main()
