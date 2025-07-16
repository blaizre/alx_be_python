#!/bin/bash/python3

i = int(input("Enter your monthly income: "))
e = int(input("Enter your total monthly expenses: "))

#Calculate Monthly Savings
s = i-e

print(f"Your monthly savings are ${s}")

#Project Annual Savings:
i = 0.05

ps = s*12+(s*12*i)

print(f"Projected savings after one year, with interest, is: ${ps}")
