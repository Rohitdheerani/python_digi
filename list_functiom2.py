x = [1,2,3,4,17,18,19,20,20,20,40,50,80,70,45,65,65]

print(x.count(20))
movies = ['avenger','hulk','iron','dr strange','3idiots','kgf']

#print(movies.index("ironman4"))

blockbuster = movies.copy()
print(blockbuster)

blockbuster.clear()
print(blockbuster)

print("after poping = ",movies.pop())
print("after poping = ",movies.pop(3))
