import socket
import sys

def server(port):        

    host = socket.gethostname()
    """Listen and receive a file, binding to the given port."""
    # Create a socket object specifying arguments to have UDP transport
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')

    # Bind the socket object to your localhost and port
    sock.bind((host,port))
    print('Socket binded')

    # Receive a filename and open a file
    data, address = sock.recvfrom(1024)
    file_name = data.decode('ascii','ignore')

    with open(file_name,'w') as f:
    # Poll for all the data that should go into the file
        while 1:
            data,address = sock.recvfrom(1024)
            if not data:
                break
            f.write(data.decode('ascii','ignore'))

    # Close the socket
    sock.close()

if __name__ == '__main__':
    if len (sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            server (port)
        except ValueError:
            print ('Usage python3 server.py port\nport must be an int')
            sys.exit(0)
    else:
            print('Usage: python3 server.py port')

