import time

def animate_intro():
    print("======================================")
    print("|                                    |")
    print("|      Welcome to the Numerology      |")
    print("|                                    |")
    print("======================================")
    time.sleep(1)
    print("This program will calculate the numerology value of your name.")
    time.sleep(1)
    print("Preparing the program...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)

def numerology_value(letter):
    # Define a dictionary to map each letter to its numerology value
    numerology_map = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
        's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
    }
    
    # Convert the letter to lowercase to match the keys in the numerology map
    letter = letter.lower()
    
    # Look up the numerology value for the letter
    if letter in numerology_map:
        return numerology_map[letter]
    else:
        return 0

def calculate_numerology_value(name):
     
   # Calculate the numerology value of a given name.
    numerology_sum = 0
    for letter in name:
        letter_value = numerology_value(letter)
        numerology_sum += letter_value
    
    # Sum the digits of the result until a single digit is obtained
    while numerology_sum > 9:
        digit_sum = 0
        for digit in str(numerology_sum):
            digit_sum += int(digit)
        numerology_sum = digit_sum
    
    return numerology_sum


def numerology_cli():
    while True:
        # Display the main menu
        print("\n=== MENU ===")
        print("1. Calculate numerology value of name")
        print("2. Exit the program")
        
        # Prompt the user to enter a choice
        choice = input("Choose an option: ")
        
        # Process the user's choice
        if choice == "1":
            # Ask the user for their name
            name = input("Enter your name: ")
            
            # Calculate the numerology value of the name
            numerology_value = calculate_numerology_value(name)
            
            # Print the result
            print("The numerology value of your name '{}' is {}.".format(name, numerology_value))
        elif choice == "2":
            # Exit the program
            print("Thank you for using the numerology program!")
            break
        else:
            # Invalid choice
            print("Invalid choice. Please choose again.")

# Run the command-line interface
if __name__ == '__main__':
    animate_intro()
    numerology_cli()

       