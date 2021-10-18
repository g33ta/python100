alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def caesar(txt,shft,direction1):
#     if direction1 == 'encode':
#         cipher_text = ''
#         for letter in txt:
#             if letter in alphabet:
#                 current_position = alphabet.index(letter)
#                 encoded_position  = current_position+shft
#                 letter = alphabet[encoded_position]
#                 cipher_text = cipher_text+letter
#         return cipher_text
#     else:
#         decoded_text = ''
#         for letter in txt:
#             if letter in alphabet:
#                 encoded_position = alphabet.index(letter)
#                 decoded_position = encoded_position-shft
#                 letter = alphabet[decoded_position]
#                 decoded_text = decoded_text+letter
#         return decoded_text
# print(caesar(text,shift,direction))

def caesar(txt,shft,direction1):
    end_text = ''
    for letter in txt:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction1 == 'encode':
                new_position  = position+shft
                letter = alphabet[new_position]
                end_text = end_text+letter
            else:
                new_position  = position-shft
                letter = alphabet[new_position]
                end_text = end_text+letter
    return (f"The {direction1}ed text is {end_text}")
print(caesar(text,shift,direction))








#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.