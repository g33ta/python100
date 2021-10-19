alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs
def encrypt(txt,shft):
    encoded_txt = ''
    for letter in txt:
        
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position+shft
            letter = alphabet[new_position]
            encoded_txt = encoded_txt+letter
    return (f"The encode text is {encoded_txt}.")
#print(encrypt(text,shift))
def decrypt(txt,shft):
    decoded_text = ''
    for letter in txt:
        if letter in alphabet:
            new_position = alphabet.index(letter)
            old_position = new_position-shft
            letter = alphabet[old_position]
            decoded_text = decoded_text+letter
    return (f"The decoded text is {decoded_text}")
if direction == 'encode':
    print(encrypt(text,shift))
else:
    print(decrypt(text,shift))
print(decrypt(text,shift))
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
