numbers = [2, 4, 6, 8, 10]

# returns square of a number
def square(number):
  return number * number

# apply square() function to each item of the numbers list
m = map(square, numbers)

print(list(m))
"""
# converting to list
squared_numbers = list(m)
print(squared_numbers)
"""
# Output: [4, 16, 36, 64, 100]
