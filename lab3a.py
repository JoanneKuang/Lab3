#!/usr/bin/env python3

# Author: Joanne Kuang
# Date: 10-03-2024
# Course: OPS455NCC
# Program: lab3a.py

'''
    Create a new script ~/ops445/lab3/lab3a.py

    Input / Output Requirements
        The script should have a Shebang line
        Below the Shebang line, add an empty line followed by a comment stating:
	# return_text_value() function
        Add an comment line and put the string Author ID:
	followed by your [seneca_id] in that line
        Add an empty line followed by the return_text_value()
	function definition that you previously entered in part 3.
        Add another empty line followed by a comment stating:
	# return_number_value() function
        Add another empty line following by the return_number_value()
	function definition that you previously entered in the shell.
        Add a couple of empty lines, following by a comment stating:
	# Main Program
        Add another couple of empty lines, followed by the statements displayed below:
'''
# return_text_value
def return_text_value():
	name = "Terry"
	greeting = "Good Morning " + name
	return greeting

# return_number_value
def return_number_value():
	num1 = 10
	num2 = 5
	num3 = num1 + num2
	return num3

# main program
if __name__ == "__main__":
	print("python code")
	text = return_text_value() # return Good Morning Terry
	print(text)
	number = return_number_value()
	print(str(number)) # return 15

'''
ouput
python code
Good Morning Terry
15
'''
