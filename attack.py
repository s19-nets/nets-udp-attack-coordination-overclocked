#! /usr/bin/env python3

import time, os, sys, re
from socket import *

pid = os.getpid()

#defaults
lAddr = ("", 50000) # listening addr+port
sAddr = ("", 50010) # sending addr+port

def usage():
    print ("usage: -l <addr:port> -s <addr:port>]")


#get parameters
#Assumning input is correct, we have the following variables
try:
    lAddr,port1 = sys.argv[2].split(":")
    sAddr,port2 = sys.argv[4].split(":")
except:
    usage()

port1 = int(port1)
port2 = int(port2)

lSocket = socket(AF_INET, SOCK_DGRAM) # listening socket
sSocket = socket(AF_INET, SOCK_DGRAM) # sending socket

print("\n")
print(pid, lAddr, ": listening on port",port1)
print(pid, sAddr, ": sending on port", port2)
print("\n")

print("dummy attack program with pid %d.  do not trust my results" % pid)

time.sleep(1)                        # sleep for 1 second

print("%d: attacking at %s" % (pid, time.asctime(time.localtime()))) # print time
