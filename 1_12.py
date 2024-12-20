categories = ['Food', 'Transport', 'Rent', 'Entertainment']
expenses = [500, 150, 1000, 200]

most_expensive = 0
index = 0
for i in range(len(expenses)):
    if expenses[i] > most_expensive:
        most_expensive = expenses[i]
        index = i

print(f'The most expensive category is: {categories[index]}')
