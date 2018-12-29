
# import the socket library 
import socket                

MSG_SIZE = 1024 #max bytes
NUM_PLAYERS = 3
connected_players = 0 

# create a socket object
s = socket.socket()         

# dict of clients and addresses
c = [0]*NUM_PLAYERS 

print ("Socket successfully created")

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345                

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port) )

# put the socket into listening mode 
s.listen(5)      
print ("socket is listening")

# a forever loop until we interrupt it or  
# an error occurs 
while True: 

    # Establish connection with all clients. 
    while(connected_players < NUM_PLAYERS - 1): # -1 to discount server
        client, addr = s.accept()      
        print ('Got connection from', addr )
        c[connected_players] = client
        connected_players += 1

        # send a confirmation message to the client.  
        client.send('Connected player'.encode()) 

    #receive whatever it says (input of player)
    action1 = c[0].recv(MSG_SIZE).decode()
    action2 = c[1].recv(MSG_SIZE).decode()
    print (action1)
    print (action2)

    break
# Close the connection with the client 
client.close() 
