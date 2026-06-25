def length(text):
    if text == "":
        return 0
    else:
        return 1 + length(text[1:])
text = input("Enter a string: ")    
print(length(text))