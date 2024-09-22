student_score = int(input("Please enter your grade : "))
if student_score >= 101 :
    print("Please verify your score.")
    quit()
if student_score > 89 :
    print("Your grade is A.")
    quit()
if student_score > 79 :
    print("Your grade is B.")
    quit()
if student_score > 69 :
    print("Your grade is C.")
    quit()
if student_score > 59 :
    print("Your grade is D.")
    quit()
else :
    print("Your grade is F")
