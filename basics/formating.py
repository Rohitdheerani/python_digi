product=input("what item did you buy?")
price=float(input("how much did you?"))
qty=int(input("how many did you buy?"))

print('you purchased',qty,product,'for',price)
#formatted string
print(f'you purchased {qty} {product}for{price}')