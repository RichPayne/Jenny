import socket, time, os, sys
#Create socket and bind
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',8989))
s.listen(10)

def nodeRecv():
    while 1:
        try:
            try:
                conn, addr = s.accept()
                conn.settimeout(10)
                print conn.recv(65000)
                conn.close()
                print "1"
            except socket.error, ex:
                conn.close()
                print ex
        except KeyboardInterrupt:
            s.close()
            print "Socket closed.\nStopped."
            sys.exit()
    
if __name__ == "__main__":
    print "Connected to localhost:8989"
    print "Listening for nodes..."
    nodeRecv()
