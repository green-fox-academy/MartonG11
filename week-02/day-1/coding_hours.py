# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52
# 

workdays = 5
daily_hours = 6
semester_weeks = 17

att1 = workdays * daily_hours * semester_weeks
print(att1)

semester_hours = 17 * 52
print(semester_hours / att1 * 100 - 100)
