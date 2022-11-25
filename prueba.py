'''
n = 5
while n  < 600:
    print('La vida es bella')
'''

numero = int(input('Escriba un numero: '))
while numero <= 10:
    print(numero)
    break
print('Intenta de nuevo')   



while True:

    try:
        numero = int(input('Escriba un numero: '))
    except ValueError:
        print("Debes escribir un número")
        continue

    if numero < 10 :
        print('Es menor que 10')
    elif numero > 10 :
        print('Es mayor que 10')
    else:
        print('Es igual que 10')
        break
    
    print('Juega de nuevo')