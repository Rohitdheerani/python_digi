name = "something serious is not HaPPening"

# formatting function

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())
print(name.casefold())

word = "python"

#leftalighn
print(word.ljust(80))
#right alighn
print(word.rjust(80))
#centre alighn
print(word.centre(80))

#fillcharexamples

print(word.ljusr(80,'_'))
print(word.rjust(80,'$'))
print(word.centre(80,'~'))

# printing a formatted table of 3
print('_'*40)
for i in range(1,11):
    r = 3** i
    print(3,'x',str(i).rjust(2),'=',r)