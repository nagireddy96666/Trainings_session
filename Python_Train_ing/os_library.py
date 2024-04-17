import os
#C:\Users\nannapur\AppData\Local\Programs\Python\Python310\Training"""
print(os.getcwd())

#print(os.listdir())

#os.chdir('C:/Users/user/Desktop/temp')

# returns a 3-tuple
for dirpath, dirname, filename in os.walk("C:/Users/user/Desktop/temp"):
    print("Current path:",dirpath)
    print('Directories: ', dirname)
    print('Files: ', filename)
    print()

