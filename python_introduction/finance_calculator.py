#!/bin/bash/python3

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculate Monthly Savings
monthly_savings = monthly_income-monthly_expenses

print(f"Your monthly savings are ${monthly_savings}")

#Project Annual Savings:

ps = monthly_savings * 12 + (monthly_savings * 12 * 0.005)

print(f"Projected savings after one year, with interest, is: ${ps}")
