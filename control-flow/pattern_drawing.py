#!/bin/bash/python3

pattern = int(input("Enter the size of the pattern: "))

while pattern >= 0:
    pattern +=1
    for i in pattern:
        print("*", end="")
        print("\n")
