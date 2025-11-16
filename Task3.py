pwd = input("Enter password: ")

if len(pwd) < 8:
    print("Weak (length must be 8 or more)")
else:
    letter = False
    digit = False
    special = False

    for ch in pwd:
        if ch.isalpha():
            letter = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if letter and digit and special:
        print("Done Your password is Strong:-",pwd)
    else:
        print("Please Change password\nyour Password is week:-",pwd,"\nUse Alphabets,Numbers,Special Characters Make Strong Password.")