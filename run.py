'''
Created By: Richard Payne
Created on: 05/08/17
Desc:       Accepts attempted connections from the Mirai scanner
            and hands the data grabbed to the string formatter
'''

import socket, os, sys, time
import mailer
import formatter as f
import fileLogger as fl

#Create socket and bind
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',23))
s.listen(10)
s.settimeout(10)

#Listens & accepts telnet connections
def recvConnection():
    while 1:
        try:
            try:
                conn, addr = s.accept()
                conn.settimeout(3)
                conn.sendall("Username: ")
                usr = conn.recv(65000)
                if not usr:
                    conn.close()
                conn.sendall("Password:")
                pw = conn.recv(65000)
                if not pw:
                    conn.close()
                conn.close()
                f.format(addr[0], usr, pw, exploit)
                fl.logExploit(exploit)
            except socket.error, ex:
                continue
        except KeyboardInterrupt:
            s.close()
            print "Socket closed.\nStopped."
            sys.exit()

if __name__ == "__main__":
    print "Jenny started..."
    recvConnection()

