def caesar_cipher(text, shift, mode='encrypt'):
 
    
    result = ""  # This variable will store the final output text
    
    # If mode is 'decrypt', we reverse the shift direction
    if mode == 'decrypt':
        shift = -shift
    
    # Loop through each character in the input text
    for char in text:
        # If the character is an uppercase English letter (A-Z)
        if char.isupper():
            # ord('A') = 65, ord('Z') = 90
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        
        # If the character is a lowercase English letter (a-z)
        elif char.islower():
            # ord('a') = 97, ord('z') = 122
            # Similar shifting logic for lowercase letters
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        
        # If it's not an alphabetic character (like space, punctuation, number)
        # we keep it unchanged
        else:
            result += char
    
    # Return the final encrypted or decrypted message
    return result
# Print the final result
# Take user input for the message
text = input("Enter your message: ")

# Take user input for the shift value (convert to integer)
shift = int(input("Enter the shift value (e.g., 3): "))

# Ask user for the mode (encrypt/decrypt)
mode = input("Do you want to 'encrypt' or 'decrypt'? ").lower()

# Call the Caesar cipher function with user inputs
output = caesar_cipher(text, shift, mode)

# Print the final result
print("\n---------------------------------")
if mode == 'encrypt':
    print("🔐 Encrypted Message:", output)
elif mode == 'decrypt':
    print("🔓 Decrypted Message:", output)
else:
    print("❌ Invalid mode selected. Please type 'encrypt' or 'decrypt'.")
print("---------------------------------")