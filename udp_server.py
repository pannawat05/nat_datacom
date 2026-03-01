from socket import *


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind to all available interfaces
serverSocket.bind(('', serverPort))

while True:
    try:
        message, clientAddress = serverSocket.recvfrom(2048)
        print(f"Received message from {clientAddress}")
        
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    except KeyboardInterrupt:
        print("\nShutting down server...")
        break

serverSocket.close()