import sys
import socket

PORT = int(sys.argv[1]) if len(sys.argv) == 2 else 6789

#create a TCP/IP socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# not sure what this is for anymore
#listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind() is used to associate the socket with the server address. The address is localhost, referring to the current server, and the port number is PORT.
listen_socket.bind(('localhost', PORT))

# Listen for incoming connections
listen_socket.listen(1)

print "Server is running ..."

'''
try:
    while True:
        # Wait for a connection
        print "while True"
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = listen_socket.accept()
except KeyboardInterrupt:
   print "\nClosing Server"
   listen_socket.close()
'''

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = listen_socket.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        '''
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(64)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
        '''
        with open('received_file.pdf', 'wb') as f:
            print 'file opened'
            while True:
                print('receiving data...')
                data = connection.recv(1024)
                print('data=%s', (data))
                if not data:
                    break
                # write data to a file
                f.write(data)

        f.close()
        print('Successfully get the file')
        connection.close()
        print('connection closed')

    except KeyboardInterrupt:
        # Clean up the connection
        connection.close()
        listen_socket.close()
