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

    elif choice == "2":
        file = open(DIARY_FILE, "r")
        lines = file.readlines()
        file.close()
        
        if len(lines) <= 1:
            print("No entries yet!\n")
        else:
            print("\n--- Your Diary Entries ---")
            for i in range(len(lines)):
                if i == 0:
                    continue
                print(str(i) + ". " + lines[i].strip())
            print()
    
    elif choice == "3":
        print("Search by: 1. Keyword  2. Date")
        search_type = input("Enter choice (1 or 2): ")
        
        file = open(DIARY_FILE, "r")
        lines = file.readlines()
        file.close()
        
        results = []
        
        if search_type == "1":
            keyword = input("Enter keyword to search: ").lower()
            for line in lines[1:]:
                if keyword in line.lower():
                    results.append(line.strip())
        
        elif search_type == "2":
            search_date = input("Enter date to search (YYYY-MM-DD): ")
            for line in lines[1:]:
                if line.startswith(search_date):
                    results.append(line.strip())
        
        if len(results) > 0:
            print("\n--- Search Results ---")
            for i in range(len(results)):
                print(str(i+1) + ". " + results[i])
            print()
        else:
            print("No results found!\n")

    elif choice == "4":
        file = open(DIARY_FILE, "r")
        lines = file.readlines()
        file.close()
        
        if len(lines) <= 1:
            print("No entries yet!\n")
        else:
            print("\n--- Your Diary Entries ---")
            for i in range(len(lines)):
                if i == 0:
                    continue
                print(str(i) + ". " + lines[i].strip())
            
            line_num = int(input("Enter line number to update: "))
            
            if line_num > 0 and line_num < len(lines):
                new_entry = input("Enter new content: ")
                current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
                lines[line_num] = current_date + " | " + new_entry + "\n"
                file = open(DIARY_FILE, "w")
                file.writelines(lines)
                file.close()
                print("Entry updated!\n")
            else:
                print("Invalid line number!\n")
    
    elif choice == "5":
        file = open(DIARY_FILE, "r")
        lines = file.readlines()
        file.close()
        
        if len(lines) <= 1:
            print("No entries yet!\n")
        else:
            print("\n--- Your Diary Entries ---")
            for i in range(len(lines)):
                if i == 0:
                    continue
                print(str(i) + ". " + lines[i].strip())
            
            line_num = int(input("Enter line number to delete: "))
            
            if line_num > 0 and line_num < len(lines):
                deleted = lines[line_num]
                lines.pop(line_num)
                file = open(DIARY_FILE, "w")
                file.writelines(lines)
                file.close()
                print("Deleted: " + deleted.strip() + "\n")
            else:
                print("Invalid line number!\n")
    
    elif choice == "6":
        file = open(DIARY_FILE, "r")
        lines = file.readlines()
        file.close()
        
        entry_count = len(lines) - 1
        print(f"\n--- Total Entries: {entry_count} ---\n")
    
    elif choice == "7":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice! Try again.\n")