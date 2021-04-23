import socket
import os
import time
import sys
f = open('ip.txt')
ip = f.read()
f.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((str(ip), 19132))
    s.send(str(sys.argv[0]+' ' + sys.argv[1]+' ' + sys.argv[2]+' ' + sys.argv[3+' ' + sys.argv[4]+' ' + sys.argv[5]).encode("utf-8"))
    s.close()     
except KeyboardInterrupt:
    sys.exit(0)
except: 
    print('[Error] Unable to connect to server')
    os.system('pause')           


