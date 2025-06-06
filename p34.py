# Write a Python program to Check Palindrome.

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
a = "A man, a plan, a canal, Panama"
if is_palindrome(a):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
