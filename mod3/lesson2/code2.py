def encrypt(text, shift):
    encryptedtext = ""
    for char in text:
        if char.isalpha():
            asciival = ord(char)
            shiftedval = asciival + shift
            if char.islower():
                if shiftedval > ord('z'):
                    shiftedval -= 26
                elif shiftedval < ord('a'):
                    shiftedval += 26
            elif char.isupper():
                if shiftedval > ord('Z'):
                    shiftedval -= 26
                elif shiftedval < ord('A'):
                    shiftedval += 26
            encryptedtext += chr(shiftedval)
        else:
            encryptedtext += char
    return encryptedtext

text = "Hello, World!"
shift = 5
encryptedtext = encrypt(text, shift)
print(encryptedtext)