import os

for file in os.listdir("C:/Users/nannapur/AppData/Local/Programs/Python/Python310/Training/Dummy_folder"):
    if file.endswith(".py"):
        print(file)
    elif file.endswith(".txt"):
        print(file)
    else:
        pass
    
