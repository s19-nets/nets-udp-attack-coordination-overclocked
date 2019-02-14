#! /usr/bin/env python3

import time, os, sys, re
from socket import *

pid = os.getpid()

#defaults
listenAddrFull = ("", 50000) # listening addr+port
sendAddrFull = ("", 50010) # sending addr+port

def usage():
    print ("usage: -l <addr:port> -s <addr:port>")


#get parameters
#Assumning input is correct, we have the following variables

try:
    lAddr, lPort = sys.argv[2].split(":")
    sAddr, sPort = sys.argv[4].split(":")
except:
    usage()

lPort = int(lPort)
sPort = int(sPort)

l = socket(AF_INET, SOCK_DGRAM) # listening socket
s = socket(AF_INET, SOCK_DGRAM) # sending socket

listenAddrFull = (lAddr, lPort)
sendAddrFull = (sAddr, sPort)

print("\n")
print(pid, lAddr, ": listening on port", lPort)
print(pid, "sending to", sAddr, "on", sPort)
print("\n")

print("dummy attack program with pid %d.  do not trust my results" % pid)

l.bind(listenAddrFull)
#l.setblocking(False)

s.bind(sendAddrFull)
#s.setblocking(False)


msg, addr = l.recvfrom(1024)


print("%d: attacking at %s" % (pid, time.asctime(time.localtime()))) # print time

