# Write a Python program to Check Palindrome.(For Number)

def is_palindrome(number):
    # Convert number to string for easy manipulation
    num_str = str(number)
    return num_str == num_str[::-1]
  
input_number = 12321
if is_palindrome(input_number):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
