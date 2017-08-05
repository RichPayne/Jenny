import mailer as m
'''
Created by: Richard Payne
Created on: 05/08/17
Desc:       Takes string from connection and extracts username, password
            and IP address of the attempted login.
'''

def format(ip, usr, pw):
    ip = ip
    usr = usr.rsplit()
    pw = pw.rsplit()

    if not usr and not pw:
        pass
    elif not usr:
        pass
    elif not pw:
        pw = "No password provided."
        m.send(ip, str(usr[0]), pw)
    else:
        m.send(ip, str(usr[0]), str(pw[0]))
