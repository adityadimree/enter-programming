def nearest_multiple(num):
    if num<4: 
        near= 4
    else:
        near = num+(4-(4%num))
    return near
num_list = []
variable = 0

def result_func():
    if variable==0:
        print("User wins !!")
    else:
        print("Computer wins !!")
    
def computers_card():
    for i in range(1,nearest_multiple(num_list[len(num_list)-1])):
        if i in num_list:
            continue
        else:
            num_list.append(i)
            if num_list[len(num_list)-1]==21:
                result_func()
def users_card():
    num_input = int(input("How many numbers do you wish to enter sir ?? "))
    flag = num_input
    while flag > 0 :
        try : 
            user_input = int(input("Please enter a integer : "))
        except:
            print("pleasse enter onlhy a single integer !!")
        if user_input in  num_list:
            print("This number is already present ! ")
            continue
        else:
            num_list.append(user_input)
            flag-=1
            if num_list[len(num_list)-1]==21:
                result_func()
            continue

while 21 not in num_list:
    if variable==0:
        computers_card()
        variable=1
        continue
    elif variable==1:
        users_card()
        variable=0
        continue