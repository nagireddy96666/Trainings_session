
import re

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\ApPython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

# Output: pattern found inside the string
