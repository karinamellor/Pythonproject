import time

def animate_intro():
    print("Bem-vindo ao programa de numerologia!")
    time.sleep(1)
    print("Este programa irá calcular o valor numerológico do seu nome.")
    time.sleep(1)
    print("Preparando o programa...")
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
    # Calculate the numerology value for the entire name
    numerology_sum = 0
    for letter in name:
        letter_value = numerology_value(letter)
        numerology_sum += letter_value
    
    return numerology_sum

def numerology_cli():
    while True:
        # Display the main menu
        print("\n=== MENU ===")
        print("1. Calcular valor numerológico do nome")
        print("2. Sair do programa")
        
        # Prompt the user to enter a choice
        choice = input("Escolha uma opção: ")
        
        # Process the user's choice
        if choice == "1":
            # Ask the user for their name
            name = input("Digite seu nome: ")
            
            # Calculate the numerology value of the name
            numerology_value = calculate_numerology_value(name)
            
            # Print the result
            print(f"O valor numerológico do seu nome '{name}' é {numerology_value}.")
        elif choice == "2":
            # Exit the program
            print("Obrigado por usar o programa de numerologia!")
            break
        else:
            # Invalid choice
            print("Opção inválida. Por favor, escolha novamente.")

# Run the command-line interface
if __name__ == '__main__':
    animate_intro()
    numerology_cli()
