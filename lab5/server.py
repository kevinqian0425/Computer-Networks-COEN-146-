import socket
import sys
import json
import random

def server(port):

    host = socket.gethostname()
    # Create a socket object given the proper socket specifications.

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket object to your localhost and port
    sock.bind((host, port))
    print('Connected to server!')

    while 1:
        data, address = sock.recvfrom(1024)
        data = data.decode('ascii', 'ignore')
        packet = json.loads(data)
        message = packet['message']
    
        checksum = 0
        for c in message:
            checksum += ord(c)
        checksum = sum([ord(c) for c in message])

        #random checksum
        if(random.random() < .5):
                checksum = -1
        if(checksum == packet['checksum']):
            print (message)
            newSeq = packet['sequence']+1
        else:
            print ('checksum error')
            newSeq = packet['sequence']
        if (packet['type'] == 'FIN'):
            print("quitting")
            break

        new_type = 'ACK'
        new_checksum = checksum
        new_message = packet['message']
        new_packet = {
            'type': new_type,
            'checksum': new_checksum,
            'message': new_message,
            'sequence': newSeq
        }
        
        string = json.dumps(new_packet).encode('ascii','ignore')
        sock.sendto(string,address) 

    # Close the socket
    sock.close()



if __name__ == '__main__':
    if len (sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            server (port)
        except ValueError:
            print('Usage: python3 server.py port\nport must be an int')
            sys.exit(0)
    else:
            print ('Usage: python3 server.py port')
