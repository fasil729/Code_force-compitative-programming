def vigenere_decrypt(ciphertext, key):
    key_length = len(key)
    plaintext = ""
    for i, char in enumerate(ciphertext):
        key_index = i % key_length
        key_char = key[key_index]
        if char.isalpha():
            char_num = ord(char) - ord('a')
            key_num = ord(key_char) - ord('a')
            decrypted_num = (char_num - key_num) % 26
            decrypted_char = chr(decrypted_num + ord('a'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

ciphertext = "ucoizsbtkxhtadcg"
possible_keys = []

# Generate all possible keys with lengths from 1 to the length of the ciphertext
for key_length in range(1, len(ciphertext) + 1):
    for i in range(26 ** key_length):
        key = ""
        for j in range(key_length):
            key += chr((i // (26 ** j) % 26) + ord('a'))
        possible_keys.append(key)

# Try decrypting with each possible key
for key in possible_keys:
    decrypted_text = vigenere_decrypt(ciphertext, key)
    if "flag" in decrypted_text:
        print("Key:", key)
        print("Decrypted Text:", decrypted_text)