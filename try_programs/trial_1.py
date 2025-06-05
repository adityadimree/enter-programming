import random
lst = range(1, 100)
lst_1 = []
while len(lst_1)<6:
    lst_1.append(random.choice(lst))
lst_1.sort()
print(lst_1)