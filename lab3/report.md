Overview

In this section, describe what you did in this lab and how you accomplished it.

Lab 3 focused on transfering and copying data via data sockets using client and server programs. To create the connection, we created a socket object and binded it toour personal host and port. We then opened a file to read and a new file to transfer from the client side and started sending data from the read file using the created socket object. The server side receives the new file first and polls which data should be transferred from the data received from the client. A successful transfer will copy all data from the transfer file.   


# Sources

In this section, use all the resources you used, people not included

Arman (because he is awesome)
Lab3 website (useful functions)
Python Software Foundation (Socket documentation for Python & Socket HowTo)
Stack Overflow

# Questions

Type your answers to the following questions on a new line after each question.

1. Describe UDP in your own words.
UDP (User Datagram Protocol) is an alternative communications protocol used primarily for establishing low latency and loss tolerating connections between applications on the Internet. UDP provides port numbers to help distinguish different user requests and a checksum capability to verify that the data arrived intact.

2. What does the bind function do? Do we need it on the client?
The bind function connects the socket object with its local address. The server side binds, so that clients can use that address to connect to the server. Clients do not need the bind function, rather it can use connect() function to connect to a remote server address. 

3. In your own words, describe what a socket is.
A network socket is an internal endpoint for sending or receiving data at a single node in a computer network. A socket is bound to a port number so that the TCP/UDP layer can identify the application that data is destined to be sent to

4. What are the Address, Family, Host, and Port variables used for in creating a socket?
A socket address comprises of an IP Address and a port number. The IP address is used for devices to identify themselves and communicate with other devices in the IP network. The port number is a way to identify a specific process to which an Internet or other network message is to be forwarded when it arrives at a server and the host, which in our case, is simply the computer connected to the network. The socket family states the communication domain in which the socket should be created. For UDP/IP sockets, we want to specify the IP address family (AF_INET) and datagram service (SOCK_DGRAM). Since there is only one form of datagram service, there are no variations of the protocol, so the last argument, protocol, is zero.

# Extra Credit Completion

Put an X in the following boxes if you completed the extra credits. Please describe your general process for doing this. What sorts of changes did you have to make in running your program?

[] Transfer a text file to your neighbor
[] Transfer an image file to your TA

# Questions about the class

1. Do you feel like you have enough Python knowledge to complete this lab?
2. Do you actually understand what we did in this lab?
3. Do the templates and stuff help? How could they be improved (No I will not just give you all the correct code)


