import json

def load_data():
    try:
        with open("youtube_2.txt", "r") as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("youtube2.txt", "w") as file:
     json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name : {video['name']} | Duration : {video['time']}")
    print("\n")
    print("*"*70)    

def add_a_video(videos):
    name = input("Please enter the video name : ")
    time = input("Please enter the video duration : ")
    videos.append({"name" : name, "time" : time})
    save_data_helper(videos)#ab ye jo add hoke new list ayi hai ise save bhi to karana hai...

def update_a_video(videos):
    list_all_videos(videos)
    index = int(input("Please enter the number of video you want to update : "))
    if 1<=index<=len(videos):
        name = input("Please enter the name of the updated video : ")
        time = input("Please enter the duration of the updated video : ")
        videos[index-1] = {'name' : name, 'time' : time}
        save_data_helper(videos)
        print("List succesfully updated !")
    else:
        print("Invalid index selected. Please try again")

def delete_a_video(videos):
    list_all_videos(videos)
    index = int(input("Please enter the video number you want to delete : "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video selected is succefully removed and the new list is saved !")
    else:
        print("Invalid number selected. Please try again.")

def main():
    videos = load_data()
    while True :
        print("\nYoutube video manager | Please select one of the given choices below.")
        print("1. List all of my videos.")
        print("2. Add a youtube video.")
        print("3. Update a youtube video.")
        print("4. Delete a youtube viideo.")
        print("5.Exit the app.")
        choice  = input("Please enter the number : ")

        match choice :
            case "1" :
                list_all_videos(videos)
            case "2" :
                add_a_video(videos)
            case "3" :
                update_a_video(videos)
            case "4" :
                delete_a_video(videos)
            case "5" :
                print("Thanks for using the app !")
                break
if __name__ == "__main__":
    main()