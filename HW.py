# This is what i am setting my alphabet to
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 '!?."

# This is telling python that this is an empty string
cipher_text = ""

# this is setting = True
add = True

# This is setting sub (subtract) = False
sub = False

# This is asking the user for an input and giving plain_text a value
plain_text = input("what would you like me to encrypt or decrypt for you? ")

# This is asking the user for an input and giving shift_key a value
shift_key = int(input("What would you like to set your shift key to? "))

# This is asking the user for an input and giving add_subtract a value
add_subtract = input("would you like to add or subtract your shift key? add/sub ")

while True:
    if add:
        for letter in plain_text:
            position = alphabet.find(letter)

            if position == -1:
                cipher_text += letter

            else:
                encrypt_position = position + shift_key
                if encrypt_position > len(alphabet)-1:
                    encrypt_position -= len(alphabet)-1

                encrypt_position = position + shift_key

                encrypt_letter = alphabet[encrypt_position]

                cipher_text += encrypt_letter
        print(f"Your cipher text is {cipher_text} ")
        break
    
    if sub:
        for letter in plain_text:
            position = alphabet.find(letter)

            if position == -1:
                cipher_text += letter

            else:
                encrypt_position = position + shift_key
                if encrypt_position > len(alphabet)-1:
                    encrypt_position -= len(alphabet)-1

                encrypt_position = position + shift_key

                encrypt_letter = alphabet[encrypt_position]

                cipher_text -= encrypt_letter

    print(f"{plain_text} is decrypted to {cipher_text}")