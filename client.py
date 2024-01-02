import socket
from threading import Thread

nickname=input("Enter a nickname: ")
# nothing
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ipAddress="127.0.0.1"
port=8000
client.connect((ipAddress,port))
print("Connected with the server successfully!")

def recieve():
    while True:
        try:
            message=client.recv(2048).decode("utf-8")
            if message=="NICKNAME":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("⚠️ An error occured! ⚠️")
            client.close()
            break

def write():
    while True:
        message=input("")
        client.send(message.encode("utf-8"))

recieveThread=Thread(target=recieve)
recieveThread.start()

writeThread=Thread(target=write)
writeThread.start()