def reciprocal_cipher(text):
    text = text.upper()
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(155 - ord(char))
        else:
            print("Error: Only letters A-Z are allowed!")
            return None  # Stop the function here
    return result

def main():
    print("Reciprocal Cipher Example") 
    choice = input("Type 'c' for CIPHER to encrypt or 'p' for PLAIN-TEXT to decrypt: ")
    user_text = input("Enter text: ")
    if choice == "c":
        print("Ciphered text:")
        output = reciprocal_cipher(user_text)
        if output is not None:
            print(output)
    elif choice == "p":
        print("Deciphered text:")
        output = reciprocal_cipher(user_text)
        if output is not None:
            print(output)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()