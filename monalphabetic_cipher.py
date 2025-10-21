import string

alphabet = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

key = "DKVQFIBJWPESCXHTMYAUOLRGZN"
#"QWERTYUIOPASDFGHJKLZXCVBNM"

encryption_dict = {alphabet[i]: key[i] for i in range(26)}
decryption_dict = {key[i]: alphabet[i] for i in range(26)}

print("Encryption dic: ", encryption_dict)

def encrypt(plaintext):
 
    ciphertext = ""  # Empty string to store the result

    # Loop through each character in the plaintext
    for char in plaintext.upper():  # Convert to uppercase for uniformity
        if char in encryption_dict:
            # Substitute the letter using the encryption dictionary
            ciphertext += encryption_dict[char]
        else:
            # If it's not a letter (e.g., space, number, punctuation),
            # we keep it unchanged.
            ciphertext += char

    return ciphertext

# Step 6: Define the decryption function
def decrypt(ciphertext):

    plaintext = ""  # Empty string to store the result

    # Loop through each character in the ciphertext
    for char in ciphertext.upper():  # Convert to uppercase for uniformity
        if char in decryption_dict:
            # Substitute the letter using the decryption dictionary
            plaintext += decryption_dict[char]
        else:
            # Keep non-alphabetic characters unchanged
            plaintext += char

    return plaintext

if __name__ == "__main__":
    # Ask the user for input
    message = input("Enter a message to encrypt: ")

    # Encrypt the message
    encrypted_message = encrypt(message)
    print("\nEncrypted Message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message)

    # Display the key mappings (optional for better understanding)
    print("\nEncryption Key Mapping:")
    for plain, cipher in encryption_dict.items():
        print(f"{plain} -> {cipher}")