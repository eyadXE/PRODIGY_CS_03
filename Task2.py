def passchecker(password):
    if len(password)<8 :
        return "The password length Must be at least 8 characters"
    fupper=False
    for i in range(len(password)):
        if password[i].isupper():
            fupper=True
            break
    if not fupper:
        return "password must cointain at least one uppercase"
    flower=False
    for i in range(len(password)):
        if password[i].islower():
            flower = True
            break
    if not flower:
        return "password must cointain at least one lowercase"
    fdigit=False
    for i in range(len(password)):
        if password[i].isdigit():
            fdigit = True
            break
    if not fdigit:
        return "password must cointain at least one digit"
    special_characters = r"!@#$%^&*(),.?\":{}|<>"
    fspecial=False
    for i in range(len(password)):
        if password[i]in special_characters:
            fspecial=True
            break
    if not fspecial:
        return "password must cointain at least on special character"
    return "Good password"
password=input("Please Entre Your Password: ")
print(passchecker(password))

