set_countries = {'col','mex','nic'}

#cuantos elementos tiene el conjunto
size = len(set_countries)
print(size)

#verificar si un dato se encuentra dentro del conjunto
print('col' in set_countries)
print('pe' in set_countries)

#add en el conjunto
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

#update para modificar el conjunto
set_countries.update({'ar','ecu','pe'})
print(set_countries)

#eliminar elementos del conjunto
set_countries.remove('col')
print(set_countries)

#da error si queres eliminar un dato que no existe
#set_countries.remove('arg')
#con discard no da error ya que sino existe 
# simplemente no lo hace sin generar el error
set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')
print(set_countries)

#elimina todos los datos del conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))