import os

#print(os.rename('abc.txt','dummy.txt'))
#print(os.remove('dummy.txt'))
#print(os.rmdir('Dummy_folder'))
#print(os.removedirs('Dummy_folder\sub'))

for dirpath, dirname, filename in os.walk('C:/Users/nannapur/AppData/Local/Programs/Python/Python310/Training'):
    print('Current path: ',dirpath)
    print('Directories: ', dirname)
    print('Files: ', filename)
    print()
