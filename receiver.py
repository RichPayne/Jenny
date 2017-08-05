import sys, os, socket

#Create socket and bind
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',8989))
s.listen(10)
s.settimeout(10)

def nodeRecv():
    try:
        conn, addr = s.accept()
        conn.settimeout(10)
        print conn.recv(65000)
    except socket.error, ex:
        print ex
    

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
    print "Connected to localhost:8989"
    print "Listening for nodes..."
    nodeRecv()
