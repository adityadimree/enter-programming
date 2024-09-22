number = int(input("Please enter an integer of your choice : "))
sum_of_even_numbers = 0
for variable in range(1, number+1) :
    if variable%2 == 0 :
        sum_of_even_numbers = sum_of_even_numbers + variable
print("Final sum of all the even numbers upto", number, "is :", sum_of_even_numbers)