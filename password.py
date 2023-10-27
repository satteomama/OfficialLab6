#Matthew Sama

def main():
    encoded = ''

    while True:
        option = int(input('1. Encode password\n2. Decode password\n3. Exit\nSelect an option: '))
        if option == 1:
            encode = str(input('Please enter your password to encode: '))
            encoded = encoder(encode)
            print('\nYour password has been encoded and stored!')
        if option == 2:
            print(f'The encoded password is {encoded}, and the original password is {decoder(encoded)}.')
        if option == 3:
            break

        





def encoder(encode):
    return_string = ''
    for i in encode:
        add = int(i) + 3
        return_string = return_string + str(add)
    return return_string

def decoder(encoded):
    return_string = ''
    for i in encoded:
        subtract = int(i) - 3
        return_string = return_string + str(subtract)
    return return_string


