#!/bin/bash/python3

size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row += 1
