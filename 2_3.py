# Weekly expenses for different categories
# ['Food', 'Transport', 'Utilities']
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# total expenses for each category
food = 0
transport = 0
utilities = 0
for row in monthly_expenses:
    food += row[0]
    transport += row[1]
    utilities += row[2]

# total expenses for each week
weeks = []
week = 0

for row in monthly_expenses:
    week += row[0] + row[1] + row[2]
    weeks.append(week)
    week = 0


total = 0
for row in monthly_expenses:
    for item in row:
        total += item

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('Week 1:', weeks[0])
print('Week 2:', weeks[1])
print('Week 3:', weeks[2])
print('Week 4:', weeks[3])
print('---------------')
print('TOTAL:', total)
