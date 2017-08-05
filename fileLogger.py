import sys, os
def log(usr, pw):
    with open("credentials.txt", "a") as f:
        f.write(usr + " " + pw + "\n")
