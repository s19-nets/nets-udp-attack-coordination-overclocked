#! /usr/bin/env python3

import time, os, sys, re
pid = os.getpid()


#get params
#Assumning input is correct, we have the following variables
addr1,port1 = sys.argv[2].split(":") #listening port
addr2,port2 = sys.argv[4].split(":") #sending port

port1 = int(port1)
port2 = int(port2)


print("\n")
print(pid,"Recieved listening port",port1)
print(pid,"Recieved sending port", port2)
print("\n")

print("dummy attack program with pid %d.  do not trust my results" % pid)

time.sleep(1)                        # sleep for 1 second

print("%d: attacking at %s" % (pid, time.asctime(time.localtime()))) # print time
