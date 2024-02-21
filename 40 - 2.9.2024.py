''' Problem Statement: Your mission, should you choose to accept it,
is to develop a function that decrypts a simple substitution cipher.
The cipher substitutes one letter for another to create a secret message.
Your function should take a string of the cipher text and a key mapping
of the substitutions and return the decrypted message.

Example: Cipher Text: "Gsv jfrxp yildm ulc" Key: {'a': 'z', 'b': 'y', 'c': 'x', ...}
(A simple reverse mapping) Output: "The quick brown fox"

Guidelines:

Utilize any programming language of your choice.

Aim for clarity and efficiency in your decryption algorithm.

Extra Challenge: Can your solution handle mixed cases and punctuation? '''


def decrypt_cipher(cipher_text, key):
    # create reverse mapping
    reverse_key = {value: key for key, value in key.items()}
    
    # initialize empty string to store decrypted message
    decrypted_message = ''
    
    # itereate through  cipher text
    for char in cipher_text:
        # if character is in the reverse mapping, replace with the corresponding decrypted letter
        if char.lower() in reverse_key:
            decrypted_message += reverse_key[char.lower()]
        else:
            # if character is not in the reverse mapping (punctuation, spaces, etc.), keep it unchanged
            decrypted_message += char
    
    return decrypted_message

# test function with given example
cipher_text = "Gsv jfrxp yildm ulc"
key = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}
decrypted_message = decrypt_cipher(cipher_text, key)
print("Decrypted Message:", decrypted_message)
