import sys, os, time

def log(usr, pw):
    with open("credentials.txt", "a") as f:
        f.write(usr + " " + pw + "\n")

def logc2(data):
    with open("log.txt", "a") as f:
        f.write((time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "] ") + data + "\n")
