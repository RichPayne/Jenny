#!/usr/bin/env python
import sys
import socket
import time
import getpass
import signal

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',23))
s.listen(10)

print "[+]-------Jenny BETA-------[+]"

#Sets up telnet sockets
def tel_con():
    while 1:
        try:
            conn, addr = s.accept()
            conn.sendall("Username: ")
            usr = conn.recv(4096)
            conn.sendall("Password:")
            pw = conn.recv(4096)
            printInfo(addr[0], usr, pw)
        except KeyboardInterrupt:
            s.close()
            sys.exit()
    
#Compiles and prints
def printInfo(remote_ip, username, password):
     ip = remote_ip
     usr = username
     pw = password
     info = (time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]" + " - " + str(ip) + " using " + str(usr) + "|" + str(pw))
     print info
     oFile(info)   

#Creates output file
def oFile(pInfo):
    oInfo = pInfo
    fileObject = open("logs.txt", "a")
    fileObject.write(oInfo + "\n")
    fileObject.close()

tel_con()
