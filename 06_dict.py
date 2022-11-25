dict = {}
for i in range (1,11):
    dict[i] = i*2
print(dict)

dict_v2 = {i:i*2 for i in range(1,5)}
print(dict_v2)

import random
countries = ['col','mex','bol','pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
print(population)

population2 = {country: random.randint(1,100) for country in countries}
print(population2)

#zip une dos listas creando un diccionario
#o una lista nueva
names = ['nico', 'zule','santi']
ages = [12,56,98]
new_list = list(zip(names, ages))
print(new_list)
print(type(new_list))
new_dict = {name:age for (name,age) in zip(names,ages)}
print(new_dict)
print(type(new_dict))

