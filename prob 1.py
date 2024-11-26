#manar shaban moubarak

steps = input("Enter the number of steps taken each day (separated by spaces): ")

steps_list = list(map(int, steps.split()))

highest_steps = max(steps_list)
lowest_steps = min(steps_list)

average_steps = sum(steps_list) / len(steps_list)

sorted_steps = sorted(steps_list, reverse=True)

print(f"Highest steps: {highest_steps}")
print(f"Lowest steps: {lowest_steps}")
print(f"Average daily steps: {average_steps:}")
print(f"Steps in descending order: {sorted_steps}")





