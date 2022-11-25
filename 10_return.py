#uso del for
sum = 0
for x in range(1,10):
    sum += x
print(sum)


#podemos guardar la operacion anterior en una 
# funcion y reutilizarla  insertandole valores
# o asignandole una variable

def sum_with_range():
    sum = 0
    for x in range(1,10):
        sum += x
    print(sum)

sum_with_range(1, 10)
sum_with_range(20, 100)

result = sum_with_range(1, 10)
print(result)
result2 = sum_with_range(result,result + 10)
print(result2)