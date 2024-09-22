
string = "How many alphabets are here ?"
count = 0
for char in string :
    if char.isalpha():
        count+=1
print(f"Total count = {count}")
