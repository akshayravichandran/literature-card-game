# Import socket module 
import socket                

MSG_SIZE = 1024 #bytes
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 
print ("Server says: "+s.recv(MSG_SIZE).decode())

#send something back
s.send("Ask player 1 for card 6 Diamonds".encode())

# close the connection 
s.close()      