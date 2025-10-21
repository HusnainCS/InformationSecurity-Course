def reciprocal_cipher(text):
    text = text.upper()
    
    result = ""
    
    for char in text:
        if 'A' <= char <= 'Z':
            reciprocal_char = chr(155 - ord(char))
            result += reciprocal_char
        else:
            result += char

    return result
   
if __name__ == "__main__":
    print("=== Reciprocal Cipher Demo ===")

    message = input("Enter message: ")
    
    # Encrypt (same as decrypt)
    cipher_text = reciprocal_cipher(message)
    print("Encrypted/Decrypted Text:", cipher_text)
    
    # Apply again to verify reciprocity
    original_text = reciprocal_cipher(cipher_text)
    print("Applying cipher again gives:", original_text)
