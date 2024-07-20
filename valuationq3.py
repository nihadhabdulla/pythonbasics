a=int(input("enter a value"))
def palindrome(s):
    if s==s[::-1]:
        print("true")
    else:
        print("false")