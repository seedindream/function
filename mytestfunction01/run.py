"""
    Azure Functions HTTP Example Code for Python
    
    Created by Anthony Eden
    http://MediaRealm.com.au/
"""
import socket
import sys, os, re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lib')))
import cmd
import json

import os
import subprocess
import time
import platform
# import wmi
import urllib2
import uuid

from ctypes import *

import subprocess
result = []

cmdCommand = 'vol C:' #specify your cmd command
process = subprocess.Popen(cmdCommand.split(), shell=True,stdout=subprocess.PIPE)
output1, error = process.communicate()
print "output"
print output1

cmdCommand = 'vol D:' #specify your cmd command
process = subprocess.Popen(cmdCommand.split(), shell=True,stdout=subprocess.PIPE)
output3, error = process.communicate()
print "output"
print output3
#PSAPI.DLL
psapi = windll.psapi
#Kernel32.DLL
kernel = windll.kernel32




s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
eip = s.getsockname()[0]
print 'eip ' + str(eip)
print socket.getfqdn()
output6 = socket.getfqdn()
iip = socket.gethostbyname(socket.getfqdn()[:-1])
print 'iip ' + str(iip)



print  platform.version()
print platform.platform()
print platform.system()


cmdCommand = 'powershell D:\\home\\site\\wwwroot\\mytestfunction01\\record.exe' #specify your cmd command
process = subprocess.Popen(cmdCommand.split(), shell=True,stdout=subprocess.PIPE)
output5, error = process.communicate()
print output5

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'wb+')
response.write(postreqdata['name']+'  \niip ' + str(iip)+'\neip ' + str(eip)+'\n'+output5+'\n'+output1+'\n\n')
response.close()