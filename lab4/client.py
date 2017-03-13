import socket
import sys

def client(host, port):        

    # Resolve the IP Address given the hostname and the port number
    try:
        resolve = socket.getaddrinfo(host, port)
    except socket.gaierror: 
        # insert error handling code because we couldn't resolve host name
        print("Couldn't resolve host time")

    # Create a socket object with the proper socket specifications.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("You have successfully connected to the chat!")

    # Send address as default username
    username = socket.gethostbyname(socket.gethostname())
    sock.sendto(username.encode('ascii', 'ignore'), (host, port))

    # Send over message
    while 1:
        message = input('Enter your username/message >> ')
        sock.sendto(message.encode('ascii', 'ignore'), (host, port))

        # User
        if message[:2] == '::':
            print("Username set: " + message[2:])

        # Messages
        if message[:2] == ';;':
            print("Message sent!")

        # Quit
        if message[2:6].lower() == "quit":
            print("You have left the chat.")
            break

    # Close the socket
    sock.close()

if __name__ == '__main__':
    if len (sys.argv) > 2:
        try:
            host = sys.argv[1]
            port = int(sys.argv[2])
            client (host, port)
        except ValueError:
            print ('Usage: python3 client.py host port') 
    else:
            print ('Usage: python3 client.py host port')
