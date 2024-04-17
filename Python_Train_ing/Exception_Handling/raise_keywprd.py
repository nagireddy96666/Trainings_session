def input_age(age):
    
    try:
        if(int(age)<=18):
           raise ZeroDivisionError
    except ValueError:
        return 'ValueError: Cannot convert into int'
    else:
        return 'Age is saved successfully'
 
 
print(input_age('23'))  # This will execute properly
print(input_age('18'))  # This will not execute properly
