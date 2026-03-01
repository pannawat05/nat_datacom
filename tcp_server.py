from socket import *
serverPort = 15000
serverSocket = socket(AF_INET, SOCK_STREAM)

# ใช้ '0.0.0.0' เพื่อเปิดรับทุก Interface
serverSocket.bind(('0.0.0.0', serverPort)) 
serverSocket.listen(1)
print("The server is ready (Listening on 0.0.0.0:15000)")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connected by: {addr}")
    sentence = connectionSocket.recv(1024).decode()
    connectionSocket.send(sentence.upper().encode())
    connectionSocket.close()