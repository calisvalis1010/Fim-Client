import socket
import os
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))
#s.connect(('212.93.106.79', 19132))
while True:
    s.send(str('0x35 1 1 0 minecraft:diamond_chestplate').encode("utf-8"))
    time.sleep(0.2)
                


