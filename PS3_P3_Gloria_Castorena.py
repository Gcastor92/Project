tryAgain = True

while tryAgain:
    userInput = input("Please enter a number or \"stop\": ")
    
    if not userInput.isdigit():
        tryAgain = False
        break
    
    num1 = int(userInput)
    
    if num1 % 2 == 0 and num1 % 3 == 0:
        print("SunDevil")
        
    elif num1 % 2 == 0:
        print("Sun")
        
    elif num1 % 3 == 0:
        print("Devil")
        
    elif num1 % 2 != 0 and num1 % 3 != 0:
        print(str(num1))
    
    print()
        
print("\nThank you for playing SunDevil, Sun Devil!")
        