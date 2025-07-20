#!/bin/bash/python3

task = input("Enter your task: ").strip()
priority = input("Enter the task's priority (high/medium/low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task. Try to finish it soon.")
        else:
            print(f"Note: '{task}' is a medium priority task. Work on it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task, but it has a deadline.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider doing it in free time.")
    case _:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
