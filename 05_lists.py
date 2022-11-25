numbers = []
for element in range(1,11):
    numbers.append(element)

print(numbers)

numbers_v2 = [element for element in range(1,11)]
print(numbers_v2)

numbers3 = []
for element in range(1,11):
    numbers3.append(element*2)
print(numbers3)

numbers4 = []
for i in range(1,11):
    if i % 2 == 0:
        numbers4.append(i*2)
print(numbers4)

numbers5 = [i*2 for i in range(1,11) if i%2 == 0]
print(numbers5)