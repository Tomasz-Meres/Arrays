###
# Returns the name of the day of the week for a given day number (1-Monday)
#

def weekday(n):
    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekdays[n-1]


print(weekday(1))
print(weekday(3))
print(weekday(7))
