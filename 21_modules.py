#el modulo sys es para preguntar acerca del SO
import sys

#mostrara en que ruta estoy ejecutando este archivo
print(sys.path)


#el modulo re es para utilizar expresiones regulares
import re
text = 'Mi numero de telefono es 311 222, codigo del pais es 57, mi número de la suerte es el 7'
result = re.findall('[0-9+]', text)
print(result)

#el modulo time sirve para obtener info sobre tiempo
import time
timestamp = time.time()
print(timestamp)
local  = time.localtime()
result = time.asctime(local)
print(result)

#modulo collections es para manejar listas
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
#cuantas veces encuentra cada numero dentro de la lista
counter = collections.Counter(numbers)
print(counter)