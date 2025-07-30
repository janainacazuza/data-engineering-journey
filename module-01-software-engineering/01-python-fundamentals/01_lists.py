tasks_of_the_day = ["Temper the steel", "Sharpen the sword", "Forge the weapon"]
print(f"Tasks for today: {tasks_of_the_day}")

tasks_of_the_day.append("Polish the blade")
print(f"Updated tasks for today: {tasks_of_the_day}")

tasks_completed = tasks_of_the_day.pop(0)
print(f"{tasks_completed} was completed.")

final_tasks = ["Sharpen the sword", "Forge the weapon", "Polish the blade"]
print("\n Showing the tasks with our automatic management system:")
for task in final_tasks:
    print(f"[ ] {task}")
