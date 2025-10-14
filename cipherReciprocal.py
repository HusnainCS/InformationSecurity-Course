print("This is a cipher reciprocal module.")
def reciprocal_cipher(text):
    return text[::-1]
if __name__ == "__main__":
    sample_text = "Hello, World!"
    print("Original:", sample_text)
    print("Reciprocal:", reciprocal_cipher(sample_text))
# This module provides a simple reciprocal cipher function.
# It reverses the input text as a form of encryption/decryption.
# The function can be tested by running the module directly.
# The reciprocal_cipher function takes a string and returns its reverse.
