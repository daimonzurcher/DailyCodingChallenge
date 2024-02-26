''' Problem Statement: Implement a set of functions that perform common bitwise operations. Your task includes creating
functions for bitwise AND, OR, XOR, NOT, LEFT SHIFT, and RIGHT SHIFT operations that mimic the behavior of these operators
in your chosen programming language.

Example Operation:

Function for Bitwise AND (bitwiseAND)

Inputs: 5 (101 in binary) and 3 (011 in binary)

Output: 1 (001 in binary)

Guidelines:

Select any programming language to showcase your bitwise operation functions.

Ensure accuracy and efficiency in your implementations.

Bonus Challenge: Demonstrate a practical application of your bitwise functions, such as setting, clearing, or toggling specific bits within an integer. '''

# needed to review the bitwise functions quite a bit for this problem...

# AND
def bitwise_AND(a, b):
    return a & b

# OR
def bitwise_OR(a, b):
    return a | b

# XOR
def bitwise_XOR(a, b):
    return a ^ b

# NOT
def bitwise_NOT(a):
    return ~a

# LEFT SHIFT
def bitwise_left_shift(a, shift):
    return a << shift

# RIGHT SHIFT
def bitwise_right_shift(a, shift):
    return a >> shift

# given example
a = 5  # in binary: 101
b = 3  # in binary: 011

# print results of all bitwise functions
print("Bitwise AND:", bin(bitwise_AND(a, b)))
print("Bitwise OR:", bin(bitwise_OR(a, b)))
print("Bitwise XOR:", bin(bitwise_XOR(a, b)))
print("Bitwise NOT:", bin(bitwise_NOT(a)))
print("LEFT SHIFT:", bin(bitwise_left_shift(a, 1)))
print("RIGHT SHIFT:", bin(bitwise_right_shift(a, 1)))