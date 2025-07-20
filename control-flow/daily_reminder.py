# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        response = f"'{task}' is a high priority task"
    case "medium":
        response = f"'{task}' is a medium priority task"
    case "low":
        response = f"'{task}' is a low priority task"
    case _:
        response = f"'{task}' has an unknown priority"

if time_bound == "yes":
    response += " that requires immediate attention today!"
else:
    response += ". Consider completing it when you have free time."

print("Reminder:", response)
