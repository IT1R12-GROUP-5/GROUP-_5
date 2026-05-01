import os
from datetime import datetime

DIARY_FILE = "PersonalDiary.txt"

if not os.path.exists(DIARY_FILE):
    file = open(DIARY_FILE, "w")
    file.write("=== This is our Personal Diary System ===\n")
    file.close()