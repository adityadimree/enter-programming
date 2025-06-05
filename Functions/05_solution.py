def greetings(name = "Boss"):
    return "Hello, "+name +"!."
    
greetings()
greetings("Tapasya")
print(greetings())
print(greetings("Tapasya"))
#so in line 4 we can see ki hamne koi bhi imput provide nhi kiya hai jb tum output dekho ge to ye conclude karoge ki ese cases me jo value hamne define krte samay variable ko di hai(see line 1) vo hi output me use hojati hai or agar hum khud hi kuch input provide kr dete hai (in line 5) toh vo output generate krne me use hojata hai.
#kya input bhi strings ke forms me dena padega ?? haa kyuki function define krte samay tumne "name" ko strings ke saath concatinate kiya hai. 