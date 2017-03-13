#Overview

Lab4 required us to create a bulletin board that allowed users to send messages to other users logged on to the
same host and port as me. I used sockets to have a client communicate to a server. 

The server establishes a socket address by assigning the local host with the gethostname() function and receiving
the port number through the command line. Clients, or the users then logon to the server by entering the host the 
server is on and the same port number used for the server on the command line. Once connected, clients can transfer 
data endlessly until they leave by typing 'Quit'. By quitting on the client side, the server will close too.

# Sources

- Lab 4 Webpage (Flowchart was extremely helpful with implementing the function)
- Arman (because he is awesome)
- Stack Overflow (with help on using certain functions such as .lower)

# Questions

What does it mean that recvfrom() is a blocking function?
A process that is blocked is one that is waiting for some event, such as a resource becoming available or the 
completion of a previous operation. recvfrom() is a blocking function because it will wait for a packet to arrive
at the socket and return once a packet is available on the socket.

How would you implement a program that allows both the client and server to send and receive messages? 
So first the client would send, the server would receive. Then the server would send and the client would receive
and so on. Don't need to actually implement, pseudocode is fine.
Use Python socket's makefile tool:
    1. Create a socket s, and create object with file-like interface using f = s.makefile() 
    2. To get text from the client and display it on the server console, write a loop with using print(f.readline())
    3. To get text from the server console and send it to the client, write a loop with f.write(raw_input('+ ') + '\n')

How does getaddrinfo() resolve the correct address? Hint: What Linux file are hosts stored in?
Network host names and IP address that are installed to the system are stored in a Linux directory.getaddrinfo()
then is able to resolve the corresponding IP address by searching the directory with the inputted
host name and the port number as parameter values.

What is the loopback address?
Loopback address is a special IP number (127.0.0.1) that is designated for the software loopback interface of a
machine. The loopback interface has no hardware associated with it, and it is not physically connected to a
network.

Programatically, how can you tell if the server has closed its connection?
When the client types 'quit', the server will receive the 'quit' message and clear all the usernames stored in the 
users dictionary. Once usernames are cleared (checked by making sure len == 0), the server program will break out
of its while-loop and close the connection by closing the socket as well. 


# Extra Credit Completion

[] Implement a chat program between you and your neighbor

[] Transfer an image file to your TA

# Questions For TA


# Comments and Feedback


