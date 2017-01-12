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
def telCon():
    while 1:
        try:
            conn, addr = s.accept()
            conn.sendall("Username: ")
            try:
                usr = conn.recv(4096)
            except socket.error, ex:
                pass
            conn.sendall("Password:")
            try:
                pw = conn.recv(4096)
            except socket.error, ex:
                pass
            printInfo(addr[0], usr, pw)
            pwLog(pw)
            usernameLog(usr)
        except KeyboardInterrupt:
            s.close()
            sys.exit()
    
#Compiles and prints
def printInfo(remote_ip, username, password):
     ip = remote_ip
     pw = password
     usr = username
     if str(usr) == "" and str(pw) == "":
         info = (time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]" + " - " + str(ip) + " using no password or username")
     else:
         usr = username.rsplit()
         pw = password.rsplit()
         try:
             info = (time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]" + " - " + str(ip) + " using " + str(usr[0]) + "|" + str(pw[0]))
         except IndexError, ex:
             info = ""
             pass
     print info
     oFile(info)   

#Creates log output file
def oFile(pInfo):
    oInfo = pInfo
    fileObject = open("logs.txt", "a")
    fileObject.write(oInfo + "\n")
    fileObject.close()

#produces dedicated passwor log
def pwLog(password):
    pw = password
    fileObject = open("pw.txt", "a")
    fileObject.write(pw + '\n')
    fileObject.close()
    
#produces dedicated username log
def usernameLog(username):
    usr = username
    fileObject = open("usr.txt", "a")
    fileObject.write(usr + '\n')
    fileObject.close()
    
telCon()
