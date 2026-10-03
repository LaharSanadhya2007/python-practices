p=input("enter a word to check palindrome:")
def palindrome(s):
    return s==s[::-1]
print(palindrome(p))