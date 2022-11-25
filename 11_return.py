#parametros por defecto y multiples return

def find_volume(length=1, width=1, depth=1):
    return length + width + depth, width,'hola'

find_volume(10,20,3)
result = find_volume(10,20,3)
print(result)


result, width, text = find_volume(width = 20)
print(width)
print(text)
print(result)