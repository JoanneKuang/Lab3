#!/usr/bin/env python3

# Author: Joanne Kuang
# Date: 10-04-2024
# Course: OPS455
# Program: lab3c.py

'''Lab 3 Inv 2 function operate '''
# Author ID: [seneca_id]
'''
def describe_temperature(temp):
    if temp > 30:
        return 'hot'
    elif temp < 0:
        return 'cold'
    elif temp == 20:
        return 'perfect'
    return 'ok'
'''
def operate(number1, number2, operator):
    # Place logic in this function
	if operator == "add":
		return number1 + number2
	elif operator == "subtract":
		return number1 - number2
	elif operator == "multiply":
		return number1 * number2

	return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    # output 15
    print(operate(10, 5, 'add'))
    # output 5
    print(operate(10, 5, 'subtract'))
    # output 50
    print(operate(10, 5, 'multiply'))
    # output error msg
    print(operate(10, 5, 'divide'))

'''
output
15
5
50
Error: function operator can be "add", "subtract", or "multiply"
'''
