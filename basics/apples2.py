amt=int(input('how much kg. of apples u wnat'))

if amt > 5:
    price=80
else:
    price = 90
total= amt * price  
print(f"you to pay Rs.{total} for {amt} kg. apples")