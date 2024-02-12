'''
Name: <Gloria Castorena>
Student ID: 1221643982
Course: IFT 101
Priblem Set: PS4
Problem: P2
Date:<02-02-2024>
'''
def main():
    # ask the user to enter integers separated by commas
    user_input = input("Please enter integers separated by commas: ")

    # Convert the input to a list of integers
    numbers = [int(num) for num in user_input.split(',')]

    #Print the total count of numbers entered
    total_count = len(numbers)
    print(f"You have entered {total_count}" " numbers.")

    #Use a while loop to count the even numbers
    even_count = 0
    i = 0
    while i < total_count:
        if numbers[i] % 2 == 0:
            even_count += 1
        i += 1

    #Use a for loop to count the odd numbers
    odd_count = 0
    for num in numbers:
        if num % 2 != 0:
            odd_count += 1

    # Print the counts to the shell
    print(f"{even_count} are even (counted with while loop).")
    print(f"{odd_count} are odd (counted with for loop).")

if __name__ == "__main__":
    main()
