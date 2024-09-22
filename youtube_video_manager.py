import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test = json.load(file)#json strings ko convert kr deta hai python objects me jese ki strings and lists. This is desrialization
            return test    
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)#is method ko do cheeze chahiye... kya dump krna hai and kaha dump karna hai. Ye python object ko convert kr deta hai json string me. This is called serialization.       
def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} | Duration: {video['time']}")
    print("\n")
    print("*"*70)
def add_a_video(videos):
    name = input("Please enter the video name: ")
    time = input("Please enter the video duration: ")
    videos.append({"name" : name, "time" : time})
    save_data_helper(videos)
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to update : "))
    if 1<=index<=len(videos):
        name = input("Please enter the video name : ")
        time = input("Please enter the video duration : ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected.") 
def delete_video(videos):
    list_all_videos(videos)#error detected.. tune function list_all_videos ko call to kar liya tha but use videos list ka input provide nhi kiya !! mind that next time bro.
    index = int(input("Please enter the video number to be deleted: "))
    if 1<=index<=len(videos):
        del videos[index-1]#ham 1 based indexing use kar rahe hai but programming to 0 based indexing se hi operate kargei.
        print("Video number", index, "succesfully deleted !")
    else:
        print("Invalid index selected.")
def main():
    videos = load_data()#hum ek method ke through kahi or se is variable me data load karayenge.
    #requirement - jese hi main program run karun my requirement is that aap constantly mujhse kuch puchte raho that's why using loop
    while True:
        print("\nYoutube Manager")
        print("1. List all of my videos.")
        print("2. Add a youtube video.")
        print("3. Update a youtube video.")
        print("4. Delete a youtube a video.")
        print("5.Exit the app.")
        choice = input("Enter your choice.")

        match choice :
            case "1":
                list_all_videos(videos)
            case "2":
                add_a_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Thank you for using the app !")
                break
            case _:
                print("Invalid choice.")        
if __name__ == "__main__":
    main()
    #is file main jis bhi function ka name main hoga vo run hojavega. this is known as dunder. 