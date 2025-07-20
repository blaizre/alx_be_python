#!/bin/bash/python3

task = input("Enter your task: ")
priority = input("(high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate action today!")
    case "low":
        if time == "no":
            print(f"Reminder: {task} is a {priority} priority task. Consider completing it when you have free time.")
