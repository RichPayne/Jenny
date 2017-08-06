'''
Created By: Richard Payne
Created on: 05/08/17
Desc:       Accepts attempted connections from the Mirai scanner
            and hands the data grabbed to the string formatter
'''

import socket, os, sys, time
import mailer
import c2
import formatter as f

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
                conn.settimeout(10)
                conn.sendall("Username: ")
                usr = conn.recv(65000)
                if not usr:
                    pass
                conn.sendall("Password:")
                pw = conn.recv(65000)
                if not pw:
                    pass
                conn.shutdown(1)
                f.format(addr[0], usr, pw)
            except socket.error, ex:
                continue
        except KeyboardInterrupt:
            s.close()
            sys.exit()

if __name__ == "__main__":
    print "Jenny started..."
    recvConnection()

