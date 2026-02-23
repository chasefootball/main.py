alphabet = "BCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 '!?."

cipher_text = ""

add = True

sub = False

plain_text = input("what would you like me to encrypt or decrypt for you? ")

shift_key = int(input("What would you like to set your shift key to? "))

add_subtract = input("would you like to add or subtract your shift key? add/sub ")

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