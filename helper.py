import subprocess
import commands
import os
import time
import sys

def get_info():
	ipOutput = commands.getoutput("curl ipinfo.io/")
	locationOutput = ipOutput.split("\n")

	NameofCity = []
	NameofCityOutput = []

	for i in range(len(locationOutput)):
			if "city" in locationOutput[i]:
				NameofCity.append(locationOutput[i])
			

	NameofCityOutput = NameofCity[0].split(":")
	NameofCityOutput[1] = NameofCityOutput[1].replace("\"", "")
	NameofCityOutput[1] = NameofCityOutput[1].replace(",", "")
	NameofCityOutput[1] = NameofCityOutput[1].replace(" ", "")
	return NameofCityOutput[1]



def get_network_services():

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


def checking_mail_application_is_running():
	

	status, output = commands.getstatusoutput("ps -x | grep Mail")

	if "/Applications/Mail.app" in output:
		subprocess.call(["killall", "Mail"])
		for i in range(10):
			print("Mail session is ending" + "." * i)
			sys.stdout.write("\033[F")
			time.sleep(0.1)
		status, output = commands.getstatusoutput("ps -x | grep Mail")
		if "/Applications/Mail.app" in output:
			return checking_mail_application_is_running()
		print "Mail session is over."
	return