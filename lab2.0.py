from random import random
add = []
for j in range(10):
    add.append(int(random()*10))
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
def wat(p):
    print("значение =", p)
wat(11)

#3)пошук послідовності елементів
def fire(sok):
    result = []
    for s in sok:
        if not result or s != result[-1][-1] + 1:
            result.append([])
        result[-1].append(s)
    return result
print (fire([1, 2, 3, 4, 8, 10, 11, 12, 17]))

#4)пошук перших п’яти мінімальних елементів
def ios():
    min1 = max(add)
    add.remove(min1)
    min2 = max(add)
    add.remove(min2)
    min3 = max(add)
    add.remove(min3)
    min4 = max(add)
    add.remove(min4)
    min5 = max(add)
    minim = (min1, min2, min3, min4, min5)[::-1]
    print(minim)
ios()

#5)пошук перших п’яти максимальних елементів
def ios():
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
ios()

#6)пошук середнього арифметичного
def mean(nums):
    print(sum(nums, 0.0) / len(nums))
mean(add)

#найменше спільне кратне
def lcm(a, b):
    lcm.multiple = lcm.multiple + b
    if ((lcm.multiple % a == 0) and (lcm.multiple % b == 0)):
        return lcm.multiple;
    else:
        lcm(a, b)
    return lcm.multiple
lcm.multiple = 0
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
if (a > b):
    LCM = lcm(b, a)
else:
    LCM = lcm(a, b)
print("НОК:")
print(LCM)

#порахувати кількість елементів
def krenj():
    temp=set(add)
    result={}
    for i in temp:
        result[i]=add.count(i)
    print(result)
krenj()

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
