my_dict = {'name':'Jack','age':26}

print(my_dict['name'])

print(my_dict.get('age'))

print(my_dict['age'])

# update 
my_dict['age'] = 27

print(my_dict)

#odd item
my_dict['address'] = 'downtown'

print(my_dict)


#create a dictionary
squares = {1:2,2:3,3:3,4:5,5:6,6:6}
print(squares.pop(4))
print(squares.popitem())
print(squares.clear())
#only .keys
for i in squares:
    print(squares[i])
#using item () functionto get both key and value
for k,v in squares.item():
    print(k,v)


 



