Download vpnSetUp.scpt and open with apple script.

Change server information with yours and run it.

To run script on Terminal:

osascript vpnSetUp.scpt

===================================================

To connect vpn:

Go to the directory you have downloaded.

Type the command to run:

python ./connection.py [Your Vpn Name]

Example:

python ./connection.py MyServer

It will quit Mail Application before connecting VPN to prevent unsusal sign-in activity.

===================================================

To disconnect vpn:

Go to the directory you have downloaded.

Type the command to run:

python ./disconnection.py

