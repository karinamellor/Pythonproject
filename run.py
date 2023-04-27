import sys

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
    # Calculate the numerology value for the entire name
    numerology_sum = 0
    for letter in name:
        letter_value = numerology_value(letter)
        numerology_sum += letter_value
    
    return numerology_sum

def numerology_cli():
    # Check if the user provided a name as a command-line argument
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:])
    else:
        # Prompt the user to enter their name
        name = input("Enter your name: ")
    
    # Calculate the numerology value of the name
    numerology_value = calculate_numerology_value(name)
    
    # Print the result
    print(f"The numerology value of your name {name} is {numerology_value}.")

# Run the command-line interface
if __name__ == '__main__':
    numerology_cli()
