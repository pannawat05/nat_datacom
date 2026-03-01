from socket import *

serverName = '49.228.131.184' #devbypan.thddns.net -> 192.168.1.114:12000
serverPort = 8861

# Create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5.0)

try:
    message = input('Input lowercase sentence: ')
    # We use sendto directly (standard UDP)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    
    print("Message sent, waiting for reply...")
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("Reply from server:", modifiedMessage.decode())

except timeout:
    print("Error: The server didn't respond. Check if the Windows script is running.")
except Exception as e:
    print(f"Error: {e}")
finally:
    clientSocket.close()