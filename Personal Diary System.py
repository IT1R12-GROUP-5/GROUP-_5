file = open("PerdonalDiary.txt", "x")
file.close()
with open("PersonalDiary.txt", "w") as file:
        file.write("This is our Personal Diary System")