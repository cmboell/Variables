"""
Program: variables.py
Author: Colby Boell
Last date modified: 1/12/2022

The purpose of this program is to set variables and have them print out
The input is quantity (integer), item (string), and size (float-point number),
and a constant variable for price.
The output should display (printed out) all the variables
"""
# variables
quantity = 7
item = "hats"
size = 8.5
# constant variable
HAT_PRICE = 12.21

# print commands to print statements
print(quantity, item, 'size:', size)
print(item + ' are $', HAT_PRICE)
"""
Expected outcomes
The first print command prints out:
7   hats  size:  8.5
using the quantity, item, and size variables

The second print command prints out:
hats are $ 12.21
using the  item and HAT_PRICE (constant) variables
"""
