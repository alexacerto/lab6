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
