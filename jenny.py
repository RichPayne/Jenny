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

#Creates XML structure
root = minidom.Document()
xml = root.createElement("root")
root.appendChild(xml)

#Creates attempt parent
attemptParent = root.createElement("Attempt")
xml.appendChild(attemptParent)

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
        consoleLogger(ip, str(usr[0]), pw)
        xmlLogger(ip, str(usr[0]), pw)
        fileLogger(str(usr[0]), pw)
    else:
        consoleLogger(ip, str(usr[0]), str(pw[0]))
        xmlLogger(ip, str(usr[0]), str(pw[0]))
        fileLogger(str(usr[0]), str(pw[0]))

#Logs information to console
def consoleLogger(ip, usr, pw):
    ip = ip
    usr = str(usr)
    pw = str(pw)
    
    print(time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]" + " - " + ip + " using " + usr + "|" + pw)

def xmlLogger(ip, usr, pw):
    ip = ip
    usr = str(usr)
    pw = str(pw)

    #Details for attemps created here
    source = root.createElement("Source")
    attemptParent.appendChild(source)
    username = root.createElement("Username")
    attemptParent.appendChild(username)
    password = root.createElement("Password")
    attemptParent.appendChild(password)
    xml_str = root.toprettyxml(indent="\t")
    attemptParent.setAttribute('Timestamp', time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]")
    source.appendChild(root.createTextNode(ip))
    username.appendChild(root.createTextNode(usr))
    password.appendChild(root.createTextNode(pw))
    
    with open("logs.xml", "w") as xml:
        xml.write(xml_str)

def fileLogger(usr, pw):
    with open("credentials.txt", "a") as f:
        f.write(usr + " " + pw + "\n")
    

if __name__ == "__main__":
    recvConnection()
