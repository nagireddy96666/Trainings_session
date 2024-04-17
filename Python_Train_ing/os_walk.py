import os

for root, dirs, files in os.walk("C:/Users/nannapur/AppData/Local/Programs/Python/Python310/Training"):
    for file in files:
        if file.endswith(".py"):
            print(file)
