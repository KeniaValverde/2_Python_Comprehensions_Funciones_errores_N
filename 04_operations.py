set_a = {'col', 'mex', 'nic','bol'}
set_b = {'pe', 'bol'}

#unir conjuntos con join o | 
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#interseccion, muestra los elemtos que hay en comun
#& nos sirve igual que la funcion intersection
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#diferencia, resta los elementos 
# del segundo conjunto al primero si se repiten
#quedando los elementos del primer conjunto
set_c = set_a.difference(set_b)
print(set_c)
print(set_a -set_b)

#diferencia simetrica, resta los elemntos que 
#se repiten
#quedan los elemntos de ambos conjuntos
#que no se repiten
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)