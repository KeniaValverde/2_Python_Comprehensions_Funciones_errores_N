#Set para crear conjuntos

set_countries = {'col','mex','nic'}
print(set_countries)
print(type(set_countries))

#Set no permite valores repetidos
set_numbers = {1,2,2,3,4,5,6}
print(set_numbers)

#Set agrupa por tipo de dato en el conjunto
set_types = {1,'hola', False, 12.12}
print(set_types)

#al usar la función set nos separa por letra la palabra
set_from_string = set('hooala')
print(set_from_string)

#para usar set en tuples tiene que estar
#en doble parentesis
set_from_tuples = set(('abc', 'cbv','as','abc'))
print(set_from_tuples)



numbers = {1,2,2,3,4,5,6}
set_numbers = set(numbers)
print(set_numbers)

#caambiamos el formato set a lista
unique_numbers = list(set_numbers)
print(unique_numbers)