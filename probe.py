import socket, time, os, sys

def probe():
    IP = ['192.81.220.63', '138.197.38.104', '139.59.139.94', '159.203.25.254', '46.101.10.77', '139.59.28.112', '128.199.197.11']
    data = ['test', 'test', 'test']
    PORT = 23
    count = 0

    for i in IP:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((i, PORT))
            for x in data:
                s.send(x)
            print i + " is ONLINE."
            s.close()
            count += 1
        except:
            print i + " is OFFLINE"
            s.close()
    print str(count) + "/" + str(len(IP)) + " online"

if __name__ == "__main__":
    probe()
