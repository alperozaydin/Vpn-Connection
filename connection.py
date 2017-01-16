import subprocess
import commands
import os
import time
import sys

from helper import get_info, checking_mail_application_is_running

myServer = sys.argv[1]

subprocess.call(["networksetup", "-connectpppoeservice", myServer])
#scpt = 'display notification "Connection Established: ' + myServer + '" with title "Vpn Connection"'
print myServer

def connection(myServer):

	for i in range(10):
	    print("Connecting" + "." * i)
	    status, output = commands.getstatusoutput("networksetup" + " -showpppoestatus " + myServer)
	    if (output == "connected"):
	        print "Connected: " + myServer
	        print "Info: "
	        os.system("curl ipinfo.io/")
	        ipOutput = commands.getoutput("curl ipinfo.io/")
	        locationOutput = ipOutput.split("\n")
	        
	        from subprocess import Popen, PIPE
	        scpt = 'display notification with title "Vpn Connection" subtitle "Connection is established: ' + get_info() + '!"'
	        p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	        stdout, stderr = p.communicate(scpt)
	        

	        break;
	    sys.stdout.write("\033[F")
	    time.sleep(1)
	return

checking_mail_application_is_running()
connection(myServer)