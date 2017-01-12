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
            usr = conn.recv(4096)
            conn.sendall("Password:")
            pw = conn.recv(4096)
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
     elif str(usr) == "":
         usr = username.rsplit()
         info = (time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]" + " - " + str(ip) + " using N/A|" + str(usr))
     elif str(pw) == "":
         pw = password.rsplit()
         info = (time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]" + " - " + str(ip) + " using " + str(pw) + "|N/A")
     else:
         usr = username.rsplit()
         pw = password.rsplit()
         info = (time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]" + " - " + str(ip) + " using " + str(usr) + "|" + str(pw))
     print info
     oFile(info)   

#Creates log output file
def oFile(pInfo):
    oInfo = pInfo
    fileObject = open("logs.txt", "a")
    fileObject.write(oInfo + "\n")
    fileObject.close()

#produces error log file
def errorLogs(errorMessage):
    error = errorMessage
    fileOnject = open("errorLogs.txt", "a")
    fileObject.write(error + "\n")
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
