price = 100
print(price)

def increment():
    price = 200
    price = price + 10
    print(price)
    return price

print(price)
increment()
price_2 = increment()
print(price_2)