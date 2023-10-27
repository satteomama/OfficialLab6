

def main():
    

    while True:
        option = int(input('1. Encode password\n2. Decode password\n3. Exit\nSelect an option: '))
        if option == 1:
            encode = str(input('Enter a password comprised of only integers: '))
            encoded = encoder(encode)
            print('Your encoded password is: ' + encoded)
        if option == 2:
            print('WIP')
        if option == 3:
            break

        





def encoder(encode):
    return_string = ''
    for i in encode:
        add = int(i) + 3
        return_string = return_string + str(add)
    return return_string


main()