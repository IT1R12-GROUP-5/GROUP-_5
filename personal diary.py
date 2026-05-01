import os
from datetime import datetime

DIARY_FILE = "PersonalDiary.txt"

if not os.path.exists(DIARY_FILE):
    file = open(DIARY_FILE, "w")
    file.write("=== This is our Personal Diary System ===\n")
    file.close()

while True:
    print("=== Personal Diary System ===")
    print("1. Add Multiple Entries")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Update Entry")
    print("5. Delete Entry")
    print("6. Line Count")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        count = int(input("How many entries do you want to add? "))
        file = open(DIARY_FILE, "a")
        for i in range(count):
            entry = input("Entry " + str(i+1) + ": ")
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
            file.write(current_date + " | " + entry + "\n")
        file.close()
        print(str(count) + " entry/entries added!\n")