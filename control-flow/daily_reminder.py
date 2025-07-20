#!/bin/bash/python3

Task = input("Enter your task: ")
Priority = input("(high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")

match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate action today!")
    case "low":
        if Time_Bound == "no":
            print(f"Reminder: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
