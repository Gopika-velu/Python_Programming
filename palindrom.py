#word = input("Enter a word: ")
#if word == word[::-1]:
#    print("Palindrome")
#else:
 #   print("Not a Palindrome")


def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])
word = input("Enter a word: ")
if palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")

