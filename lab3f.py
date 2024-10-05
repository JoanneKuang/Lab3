#!/usr/bin/env python3

# Author: Joanne Kuang
# Date: 10-05-2024
# Course: OPS445
# Program: Lab3f.py

# Place my_list below this comment (before the function definitions)
# declare my_list and have the values 1, 2, 3, 4, 5
my_list = [1, 2, 3, 4, 5]


def add_item_to_list(ordered_list):
	# Appends new item to end of list with the value (last item + 1)
	ordered_list.append(ordered_list[-1]+1)

def remove_items_from_list(ordered_list, items_to_remove):
	# Removes all values, found in items_to_remove list, from ordered_list
	for values in items_to_remove:
		if values in ordered_list:
			ordered_list.remove(values)

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)

'''
ouput
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 7, 8]
'''
