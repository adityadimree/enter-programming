import random
test_case = int(input())
while test_case>0:
    int1 = int(input())
    lst = range(1, 100)
    lst_1 = []
    while len(lst_1)<int1+1:
        lst_1.append(random.choice(lst))
    lst_1 = lst_1.sort()
    for i in lst:
        for k in lst_1:
            

    
