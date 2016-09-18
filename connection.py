import subprocess
import commands
import os
import time
import sys

myServer = sys.argv[1]

subprocess.call(["networksetup", "-connectpppoeservice", myServer])

print myServer

def Connection(myServer):

	for i in range(10):
	    print("Connecting" + "." * i)
	    status, output = commands.getstatusoutput("networksetup" + " -showpppoestatus " + myServer)
	    if (output == "connected"):
	        print "Connected: " + myServer
	        print "IP Address: "
	        os.system("curl ipecho.net/plain ; echo")
	        break;
	    sys.stdout.write("\033[F")
	    time.sleep(1)
	return


def checkingMailApplicationIsRunning():
	

	status, output = commands.getstatusoutput("ps -x | grep Mail")

	if "/Applications/Mail.app" in output:
		subprocess.call(["killall", "Mail"])
		for i in range(10):
			print("Mail session is ending" + "." * i)
			sys.stdout.write("\033[F")
			time.sleep(0.1)
		status, output = commands.getstatusoutput("ps -x | grep Mail")
		if "/Applications/Mail.app" in output:
			return checkingMailApplicationIsRunning()
		print "Mail session is over."
	return



checkingMailApplicationIsRunning()
Connection(myServer)