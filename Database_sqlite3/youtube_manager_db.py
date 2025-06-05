import sqlite3

conn = sqlite3.connect('youtube_videos.db')#ye brackets me database ka name hai. yaha pe hamne ek connection link set up kri hai jese mines se factory ek road link setup krti hain.
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )

''')#error alert !!! you forgot the commas in the above part in line 6 and 7 after null.
def list_videos():
    print("*"*80)
    #we will use cursor object everywhere... yhi object database se query krta hai...
    cursor.execute("SELECT * FROM videos")
    #is query ka response ata hai dataase se sara ek baar me and cursor object us data ko hold krke rakhta hai, now it depends on us ki ham use kitna data lena chahte hai ek baar me.
    for index, name, time in cursor.fetchall():
        print(f"{index}. Name : {name} | Duration : {time}")
    print("*"*80)
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES(?, ?)", (name, time))
    conn.commit()#this commit ensures that new data has been succesfully saved in table.
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))#yaha pe ye comma dena important hai... as database ke andar sirf tuple values hi accept hoti hai. or braces ke inside sirf ek object porvide karane se vo tuple me nhi mana jata. so ek commma laga ke chodh dete hai.
    conn.commit()
def main():
    while True:
        print("\n Youtube video manager app | Please select oneof the given choices.")
        print("1. List all videos.")
        print("2. Add a video.")
        print("3. Update a video.")
        print("4. Delete a video.")
        print("5. Exit the app.")
        choice = input("Please enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("PLease enter the name of the video: ")
            time = input("Please enter the time duration of the video: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Please enter the video id to be updated: ")
            name = input("PLease enter the name of the video: ")
            time = input("Please enter the time duration of the video: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Please enter the video id to be deleted: ")
            delete_video(video_id)
        elif choice == "5":
            print("Thank you for using the app !!")
            break
        else:
            print("Invalid choice.")
#jo connection hamne establish kiya hai use ham close kara denge is se database ke corrupt hone ke chances kam ho jate hai and memory ke liye bhi favourable ho raha hai.
    conn.close()

if __name__ == "__main__":
    main()