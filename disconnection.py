import subprocess
import commands
import os
import time
import sys

from helper import get_info, get_network_services


def disconnection(myServer):

	subprocess.call(["networksetup", "-disconnectpppoeservice", result])
	for i in range(10):
		print("Disconnecting" + "." * i)
		sys.stdout.write("\033[F")
		time.sleep(0.1)
	status, output = commands.getstatusoutput("networksetup" + " -showpppoestatus " + result)
	if output == "Connected":
		return Disconnection(myServer)
	print "Disconnected: " + result
	from subprocess import Popen, PIPE
	scpt = 'display notification with title "Vpn Connection" subtitle "Connection is over: ' + where_is + '!"'
	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate(scpt)

	return

def check_connection():
	global result
	for i in range(len(myServer)):
		status, output = commands.getstatusoutput("networksetup" + " -showpppoestatus " + myServer[i])
		if (output == "connected"):
			result = myServer[i]
	return


myServer = get_network_services()

result = "a"

isDisconnected = False

check_connection()
where_is = get_info()
disconnection(myServer)


