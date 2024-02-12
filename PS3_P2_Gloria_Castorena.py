tryAgain = "y"

while tryAgain == "y":    
    string1 = input("Enter the word to check for palindrome: ")
    string2 = ""
    for i in reversed(string1):
        string2 += i
    
    if string1 == string2:
        print(f"Yes, {string1} is a palindrome")
    else:
        print(f"No, {string1} is not a palindrome")
    
    tryAgain = input("Would you like to try again? (y/n): ")

print("Thank you for using my palindrome checker!")