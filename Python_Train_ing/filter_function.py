numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True
    return False

# Extract elements from the numbers list for which check_even() returns True
m = filter(check_even, numbers)

print(list(m))
# Output: [2, 4, 6, 8, 10]
