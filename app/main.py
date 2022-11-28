import mod

keys, values = mod.get_population()
print(keys, values)

print(mod.A)

data = [
    {
        'Country':'Colombia',
        'Population':300
    },
    {
        'Country':'Bolivia',
        'Population':300
    }
]

country = input('Type Country => ')
Result = mod.population_by_country(data,country)
print(Result)