#password strength checker.
password = input("Please enter your password\nPassword: ")

if len(password) < 6 :
    strength = "Weak"
elif len(password) <=15 :
    strength = "Medium"
else :
    strength = "Strong"
print("Strength of your password is", strength)

    
