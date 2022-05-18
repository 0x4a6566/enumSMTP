#!/usr/bin/python

import socket, sys, re

print "\nEnumerating Users\n"

if len(sys.argv) != 2:
        print "\nExample: python2 enumSMTP.py 172.20.10.5"
        sys.exit(0)

file = open("users.txt")

for line in file:
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect((sys.argv[1], 25))
	banner = tcp.recv(1024)

	tcp.send("VRFY "+line)
	user = tcp.recv(1024)
	if re.search("252", user):
		print "User found: " +user.strip("252 2.0.0")

