import subprocess
import commands
import os
import time
import sys



def getNetworkdServices():

	output = commands.getoutput("networksetup" + " -listallnetworkservices")

	output = output.split("\n")

	statusOutput = []
	myServerList = []

	for i in range(len(output)):
		statusOutput.append(commands.getoutput("networksetup" + " -showpppoestatus " + output[i]))


	for i in range(len(statusOutput)):
		if "disconnected" and "connected" in statusOutput[i]:
			myServerList.append(output[i])



	return myServerList


myServer = getNetworkdServices()

result = "a"

isDisconnected = False

def checkConnection():
	global result
	for i in range(len(myServer)):
		status, output = commands.getstatusoutput("networksetup" + " -showpppoestatus " + myServer[i])
		if (output == "connected"):
			result = myServer[i]
	return


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
	return



checkConnection()
disconnection(myServer)


