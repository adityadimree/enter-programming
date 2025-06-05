#Weather activity suggestor.
weather_type = input("Please describe today's weather conditions in terms of these three terms :\n1.Sunny\n2.Rainy\n3.Snowy\nInput : ")
if weather_type == "Sunny" : 
    print("Go for a walk.")
elif weather_type == "Rainy" :
    print("Read a book.")
elif weather_type == "Snowy" :
    print("Build a snowman.")
else :
    print("Please check the weather again.")
    quit