# This is what i am setting my alphabet to
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 '!?."

# This is telling python that this is an empty string
cipher_text = ""

# this is setting = True
add = True

# This is setting sub (subtract) = False
sub = False

shift_nums = 0

chioce = input("would you like me to encrypt or decrypt for you? e/d ")
if chioce == "e":
    print("sure! I will encrypt for you!")
if chioce == "d":
    print("Oh boy you chose the hard way ")

# This is asking the user for an input and giving plain_text a value
plain_text = input(f"What would you like me to {chioce} for you? ")

# This is asking the user for an input and giving shift_key a value
shift_key = int(input("What would you like to set your shift key to? "))

# This is asking the user for an input and giving add_subtract a value
add_subtract = input("would you like to add or subtract your shift key? add/sub ")

if chioce == "e":
    while True:
        if add:
            for letter in plain_text:
                position = alphabet.find(letter)

                if position == -1:
                    cipher_text += letter

                else:
                    encrypt_position = position + shift_key
                    if encrypt_position > len(alphabet)-1:
                        encrypt_position %= len(alphabet)-1

                    encrypt_position = position + shift_key

                    encrypt_letter = alphabet[encrypt_position]

                    cipher_text += encrypt_letter
            print(f"Your encrypted cipher text is {cipher_text} ")
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
            break

if chioce == "d":
    while True:
        cipher_text = ""
        
        for letter in plain_text:
            position = alphabet.find(letter)

            if position == -1:
                cipher_text += letter
            else:
                decrypt_position = position - shift_nums
                decrypt_position %= len(alphabet)
                cipher_text += alphabet[decrypt_position]

        print(cipher_text)
        ask = input("Is this readable? y/n ")

        if ask == "y":
            print(f"You need the shift key {shift_nums} times ")
            break

        shift_nums += 1