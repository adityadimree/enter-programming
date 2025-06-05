#Pet food recomendation
pet_species = str(input("Please tell weather your pet is a Dog or a Cat : "))

pet_species1 = pet_species.lower()

if pet_species1 == "dog" :
    age = int(input("enter the age of your Dog : ")) 
    if age < 2 :
        print("Puppy pet food is recommended.")
    else :
        print("Normal dog food is recommended.")
elif pet_species1 == "cat" :
    age = int(input("Please enter the age of your cat : "))
    if age > 5 :
        print("Senior cat food is recommended.")
    else :
        print("Baby cat food is recommended.")
else : 
    quit("This programm only recommends for dog and cats.")
    
    


   
