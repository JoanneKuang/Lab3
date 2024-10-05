#!/usr/bin/env python3

# Author: Joanne Kuang
# Date: 10-04-2024
# Course: OPS455
# Program: lab3d.py

# import module
import os

# function called free_space()
def free_space():
    	# this will launch linux command as a new process
	command = "df -h | grep '/$' | awk '{print $4}'"
	# this will get and run output
	output = os.popen(command).read()
	return output.strip()

if __name__ == "__main__":
	# return the disk space
    	print(free_space())

#output 7.1G

