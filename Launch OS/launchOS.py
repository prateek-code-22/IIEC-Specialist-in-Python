# COMMANDS TO ACTION PAGE:

#! /usr/bin/python3
print("Content-type: index/html")
print()

import os
import subprocess
import cgi 

command = cgi.FieldStorage()
value = command.getvalue('command')

query = value
query = query.lower()

# START COMMANDS HERE:
if ("run" in query) or ("open" in query) or ("launch" in query) or ("enable" in query):
    
    if ("docker" in query) or ("container" in query):
        ret = subprocess.getoutput('sudo systemctl start docker')
        print("DOCKER SERVICE STARTED...")
        
    elif ("firewall" in query) or ("firewalld" in query):
        ret = subprocess.getoutput("sudo systemctl start firewalld")
        print("FIREWALL STARTED...")
        
    elif "date" in query:
        ret = subprocess.getoutput("date")
        print(ret)
    
    elif "calender" in query:
        ret = subprocess.getoutput("cal")
        print(ret)

    elif "ifconfig" in query:
        ret = subprocess.getoutput("ifconfig")
        print(ret)
    
    
# STOP COMMANDS HERE:
elif ("shut" in  query) or ("stop" in query) or ("disable" in query):
    
    if ("docker" in query) or ("container" in query):
        ret = subprocess.getoutput('sudo systemctl stop docker')
        print("DOCKER SERVICES STOPPED...")

    elif ("firewall" in query) or ("firewalld" in query):
        ret = subprocess.getoutput('sudo systemctl stop firewalld')
        print("FIREWALL STOPPED...")
        
else:
    print("Sorry! please check your Command again")

