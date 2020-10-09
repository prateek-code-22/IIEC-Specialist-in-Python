#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi 

form = cgi.FieldStorage()

osname = form.getvalue("x")
imageName = form.getvalue("i")

cmd = "sudo docker run -i -t --name {0} {1}".format(osname,imageName)

op = sp.getstatusoutput(cmd)

print("OS Name: ",osname)
print("OS Image Name:",imageName)

status = op[0]
out = op[1]

if status== 0:
	print("OS launched {} ...".format(osname))
else:
	print("Error occured: ")
	print("\n")





''' USE OF FORMAT()IN PRINT.
example to use input data in cmd query
x= 45
print("turn iron to {0} degree".format(x)) 
O/P - turn to 45 degree
'''
