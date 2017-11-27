current_hours = 14
current_minutes = 34
current_seconds = 42



# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables


myseconds = (current_seconds + current_minutes * 60 + current_hours * 3600)

day = 24 * 3600

remaining = day - myseconds

print(str(remaining))