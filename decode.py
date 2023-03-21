def decode(encoded_password):
    list_pass = list(encoded_password)
    for i in range(0, len(list_pass)):
        list_pass[i] = str(int(list_pass[i]) - 3)
    new_list = ''.join(list_pass)
    return new_list
