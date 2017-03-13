import socket
import sys

def server(port):

    host = socket.gethostname()
    # Create a socket object given the proper socket specifications.

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket object to your localhost and port
    sock.bind((host, port))

    print('Chat opened!')

    users = {}

    while 1:
        data, address = sock.recvfrom(1024)
        message = data.decode('ascii', 'ignore')

        # Username
        if message[:2] == '::':
            users[address] = message[2:]
            print( 'client has set username to: ' + users[address])

        # Message
        if message[:2] == ';;':
            if address in users:
                print(users[address]+ ": " + message[2:])
            else:
                print(str(address)+ ": "+ message[2:])

            # Quit
            if message[2:6].lower() == 'quit':
            # Close chat if user quits right away
                if len(users) == 0:
                    break
                if address in users:
                    del users[address]
                # Close chat if no users left
                if len(users) == 0:
                    print('Chat closed.')
                    break


    # Close the socket
    sock.close()



if __name__ == '__main__':
    if len (sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            server (port)
        except ValueError:
            print("Error\n")
            sys.exit(0)
    else:
            print ('Usage: python3 server.py port')
