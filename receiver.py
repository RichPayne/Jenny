import sys, os, socket

#Create socket and bind
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',8989))
s.listen(10)
s.settimeout(10)


def nodeRecv():
    try:
        try:
            conn, addr = s.accept()
            conn.settimeout(10)
            print conn.recv(65000)
        except socket.error, ex:
    except KeyboardInterrupt:
        s.close()
        sys.exit()
    

#Logs information to console
def consoleLogger(ip, usr, pw):
    ip = ip
    usr = str(usr)
    pw = str(pw)
    
    print(time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]" + " - " + ip + " using " + usr + "|" + pw)

def fileLogger(usr, pw):
    with open("credentials.txt", "a") as f:
        f.write(usr + " " + pw + "\n")


if __name__ == "__main__":
    print "Listening for nodes..."
    nodeRecv()
    
