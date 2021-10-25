#1)швидке сортування
def quick_sort(s):
    if len(s) <= 1:
        return s
    el = s[0]
    left = list(filter(lambda x: x < el, s))
    centre = [i for i in s if i == el]
    right = list(filter(lambda x: x> el, s))
    return quick_sort(left) + centre + quick_sort(right)
print(quick_sort([23,4,355,35,5,67,8,9,654,34,11]))

#2)пошук елементу за значенням
q = [1,2,3,5,6,7,8,11]
for i in q:
    if i == 11:
     print(i)

#3)пошук послідовності елементів
c = [1,2,3,4,5,6,7,8,9]
for idx, a in enumerate(c):
    if c [idx:idx+4] == [a,a+1,a+2,a+3]:
        print([a, a+1,a+2,a+3])
        break

#4)пошук перших п’яти мінімальних елементів
from random import random
add = []
for j in range(10):
    add.append(int(random()*10))
print(add)
def quick_sort(s):
    if len(s) <= 1:
        return s
    el = s[0]
    left = list(filter(lambda x: x < el, s))
    centre = [i for i in s if i == el]
    right = list(filter(lambda x: x> el, s))
    return quick_sort(left) + centre + quick_sort(right)
print(quick_sort(add[:5]))

#5)пошук перших п’яти максимальних елементів
max1 = max(add)
add.remove(max1)
max2 = max(add)
add.remove(max2)
max3 = max(add)
add.remove(max3)
max4 = max(add)
add.remove(max4)
max5 = max(add)
maxus = (max1, max2, max3, max4, max5)[::-1]
print(maxus)

#6)пошук середнього арифметичного
print(sum(add)/len(add))

#найменше спільне кратне
print([i for i in add if i >=1])
from functools import reduce
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
res = reduce(lcm, add)
print(res)

#порахувати кількість елементів
temp=set(add)
result={}
for i in temp:
    result[i]=add.count(i)
print(result)

#циклічний здвиг
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

print(add)
shift(add, -2)
print(add)
shift(add, 3)
print(add)