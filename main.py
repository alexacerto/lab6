from decode import decode
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


def encode(password):
    # encoding password by adding each digit by 3
    num_lst = []    # creating list to hold each digit
    encoded_password = ""   # empty string
    for num in password:
        num_lst.append(num) # list of digits
    num_lst = [int(i) for i in num_lst]
    for i in range(len(num_lst)):
        num_lst[i] += 3    # adding three to each digit
        if num_lst[i] >= 10:
            num_lst[i] -= 10   # if digit >= to 10, replace with ones value
        else:
            continue
    for num in num_lst:
        encoded_password += str(num)    # string of converted digit
    return encoded_password


if __name__ == '__main__':
    while True:
        print_menu()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()

        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
            pass

        elif option == 3:
            break
