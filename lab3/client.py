import socket
import sys

def client(host, port, file_name):
    """ Transfer file_name to a server hopefully listening at (host, port)."""

    try:
        # Resolve the IP Address given the hostname and the port number using getaddrinfo
        sockaddress = socket.getaddrinfo(host,port)

    except socket.gaierror: 
        # insert error handling code because we couldn't resolve host name
        print('Failed to create file') 
        sys.exit()

    # Create a socket object with the proper socket specifications.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send over a different file name than what we're reading encoded properly
    sock.sendto(('copy'+file_name).encode('ascii','ignore') , (host,port))

    # Open the file to transfer and start sending data using the created socket object
    # At the end, you should send a control message, just an empty string to notify the end of file
    with open(file_name, 'r') as f:
        
        print('Sending line...')

        while 1:
            data = f.read(1024).encode('ascii', 'ignore')
            if not data:
                sock.sendto("".encode('ascii','ignore'),(host,port))
                break
            sock.sendto(data,(host,port))

    print("File Sent")


    # Close the socket
    sock.close()

if __name__ == '__main__':
    if len (sys.argv) > 2:
        try:
            host = sys.argv[1]
            port = int(sys.argv[2])
            file_name = sys.argv[3]
            client (host, port, file_name)
        except ValueError:
            print ('Second argument should be an integer representing port number')

    else:
            print ('Usage: python3 client.py host port')



