#higher order function

def increment(x):
    return x + 1

#lo mismo de arriba pero con lambda
increment2 = lambda x: x + 1

def high_ord_func(x, func):
    return x + func(x)

#la funcion de arriba pero con lambda
high_ord_func2 = lambda x, func: x + func(x)

result = high_ord_func(2,increment)


#2 + (2+1)

print(result)

#Llamar lambda e imprimir
result = high_ord_func2(2,increment2)
print(result)

result = high_ord_func2(2,lambda x: x + 2)
print(result)

result = high_ord_func2(2,lambda x: x * 5)
print(result)