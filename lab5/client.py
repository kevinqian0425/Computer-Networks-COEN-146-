import socket
import sys
import json

def client(host, port):        

    # Resolve the IP Address given the hostname and the port number
    try:
        resolve = socket.getaddrinfo(host, port)
    except socket.gaierror: 
        # insert error handling code because we couldn't resolve host name
        print("Couldn't resolve host time")

    # Create a socket object with the proper socket specifications.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket successfully initialized')

    skip = False
    sent_data = True
    sequence = 0
    is_FIN = False

    while 1:
        #deserialize
        while skip:
            data,address = sock.recvfrom(1024)
            message = data.decode('ascii','ignore')
            packet = json.loads(message)

            #checksum incorrect
            if(packet['checksum']== -1):
                print('checksum not matching, re sending')
                sent_data = False 
                skip = True
                break
            else: 
                print('packet received')
                sent_data = True
                sequence = sequence +1 
                skip = True
                break

        if sent_data:
            message = input('input message: ')
        else:
            message = packet['message']
        
        #checksum
        checksum = 0 
        for c in message:
            checksum += ord(c)
        checksum = sum([ord(c) for c in message])

        if message == 'FIN':
            sort = 'FIN'
            is_FIN = True
        else: 
            sort = ' '

        packet = {
            'type': sort,
            'checksum': checksum,
            'message': message,
            'sequence': sequence
        }
        
        #serialize
        string = json.dumps(packet).encode('ascii','ignore')
        sock.sendto(string,(host,port))
        skip = True

        if is_FIN == True:
            print('client has left the chat')
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
