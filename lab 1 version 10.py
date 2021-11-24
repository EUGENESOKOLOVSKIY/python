#задание 1
import math
a = float(input("введите число"))
b = math.degrees(math.cos(a))
z = b**2 + b**4
print(z)
#задание 2
s = float(input("Введите размер стипендии = "))
b = float(input("Введите размер расходов ="))
o = 10*s
p = 0 
e = 1
while e <= 10:
    e = e + 1
    p = p + b
    b= b*1.05
if p <= o:
    print("Стипендии хватит")
else:
    print("Нужно попросить у родителей",p-o)
# задание 3
fem = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

print(min([x for x in fem if x > 0])) #задание а

f = lambda x: x[0] * f(x[1:]) if x else 1 # задание б
print (f([a for a in fem if a % 2]))

print([i for i in fem if i < 0])   #задание с

    
