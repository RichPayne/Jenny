import socket
#Create socket and bind
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',8989))
s.listen(10)

def nodeRecv():
    while 1:
        try:
            conn, addr = s.accept()
            conn.settimeout(10)
            print conn.recv(65000)
        except socket.error, ex:
            print ex
    
if __name__ == "__main__":
    print "Connected to localhost:8989"
    print "Listening for nodes..."
    nodeRecv()
