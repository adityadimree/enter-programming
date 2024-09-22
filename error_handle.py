file = open("youtube.txt", "w")

try: 
    file.write("youtube.txt")
finally:
    file.close()

with open("youtube.txt", "w") as file :
    file.write("chai aur Python")
    