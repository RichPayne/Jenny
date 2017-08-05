import socket
#Create socket and bind
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',8989))
s.listen(10)

def nodeRecv():
    try:
        print "Connected to localhost:8989"
        conn, addr = s.accept()
        conn.settimeout(10)
        print conn.recv(65000)
    except socket.error, ex:
        print ex
    
if __name__ == "__main__":
    print "Listening for nodes..."
    nodeRecv()
