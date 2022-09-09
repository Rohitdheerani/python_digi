#syntax
# def fun_name([Parameter]):
#         statements
3#        [return expression]

# defining
def hello():
    print('👋ohello')
    print('worls🌍')
# calling or using
hello()    
hello()

def  greetings(message):
    print('👋',message)

greetings('world') 
greetings('hola amigos')
greetings('bonjour amis')
greetings('namaste dosto')

def calc_area(w, h):
    area = w * h
    print('area:',area)

calc_area(10, 20)
calc_area(3, 5)
calc_area(100, 200)    

def cal_area_v2(w, h):
    area = w * h
    return area

print(cal_area_v2(10, 20))
print(cal_area_v2(3, 5))

# storing return value in variable
ans = cal_area_v2(10, 20)
print(ans)

#using return values in a expression
ans = cal_area_v2(3, 5) + cal_area_v2(10, 2)
print(ans)