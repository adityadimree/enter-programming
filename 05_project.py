#Welcome to my personal text editor. The goal is to create a file and write in it.
from file_searcher import file_founder
def create_write():
    #Create a new file. Raises an error if a file already exists
    print("What would you like to name your file ?")
    name = input("\n> ")
    try:
        file = open(name, "x+")
        print("\nWrite whatever you want to !")
        content = input("\n> ")
        file.write(content)
        print("\nFile has been written successfully !")
        file.close()
    except:
        print("File already exists !")
        quit()

def add_existing():
    # Add something to an existing file. Raises an error if the file does not exist. As user wants to "add", it does not overwrites the present content.
    print("\nWhat is the name of your file ?")
    name = str(input("\n> "))
    if file_founder(name):
            file = open(name, "a")
            print("\nWrite whatever you want to !")
            content = input("\n> ")
            file.write(content)
            file.close()
            print("\nYour file has been updated !")
    else:
        print("It appears that the file you are looking for does not exists !")

def read_file():
     #The goal is to put on display whatever is present in the file.
    print("\nGive me the name of the file you want to read ;>")
    file_name=str(input("\n> "))
    try:
        file = open(file_name, "r")
        content = file.read()
        print("\nHere is your content :>")
        print(content)
    except:
        print("ERR, the file you are looking for does not exists !")
        quit()

def main():
    while True:
        print("\n")
        print("*"*80)
        print("\nWelcome to my personal text editor.")
        print("\nWhat do you wish to do today ?")
        print("\n1. Create a new file and write in it.")
        print("\n2. Add something to an existing file.")
        print("\n3.Read a file.")
        print("\n4. Exit")
        choice = int(input("\n> "))
        match choice:
            case 1:
                create_write()
            case 2:
                add_existing()
            case 3:
                read_file()
            case 4:
                print("\n")
                print("*"*80)
                print("\nThank you for using my editor !\nBye !")
                quit()
            case _:
                print("\nInvalid choice. Try again !")


if __name__ == "__main__":
    main()

