from Crypto.Cipher import AES

def main():
    print('\n[E]nter a new password')
    print('[R]etrieve an old password')
    print('[Q]uit')
    menu_input = input('')
    if menu_input is 'E' or menu_input is 'e':
        encrypt_pass()
    elif menu_input is 'R' or menu_input is 'r':
        decrypt_pass()
    elif menu_input is 'Q' or menu_input is 'q':
        quit()
    else:
        print('Enter a valid letter')  # fix later



def encrypt_pass():
# what is being encrypted
    user_data = input('Type the text to be encrypted: ')

# converting key to bytes
    data = bytes(user_data, "utf-8")

# User input master password
    user_key = input('Input you master key: ')

# Making user password accepted by AES
    for x in range(len(user_key), 16):
        user_key = user_key + '0'

# converting key to bytes
    key = bytes(user_key, 'utf-8')

# Encrypting the data
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

# Writing the encrypted data to file
    file_out = open("encrypted.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()
    print("Encryption successful")

    main()

def decrypt_pass():
#  User input master password to decrypt
    user_key = input('Input your master key: ')
# Making user password accepted by AESr
    for x in range(len(user_key), 16):
        user_key = user_key + '0'
    key = bytes(user_key, 'utf-8')
    file_in = open("encrypted.bin", "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    print("Your password is:%s" %data)

    main()

def test():
    print("this is a test")

#  version = 1.0
#  print('Password Protector v%s' % version)
main()