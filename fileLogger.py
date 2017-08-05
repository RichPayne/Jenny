import sys, os
def fileLogger(usr, pw):
    with open("credentials.txt", "a") as f:
        f.write(usr + " " + pw + "\n")
