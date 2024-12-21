import random

passwords_list = []
2
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

choice = input("Would you like to (1) type your own password or (2) generate one? Enter 1 or 2: ")

if choice == "1":
    password = input("Type your password: ")
    if len(password) < 8:
        print("Password is too short")
    else:
        passwords_list.append(password)
        print("Password created successfully")

elif choice == "2":
    length = int(input("Enter desired password length: "))
    generated_password = ""
    for i in range(length):
        generated_password += random.choice(characters)
    print("Generated password:", generated_password)
    passwords_list.append(generated_password)
    print("Password created successfully")


        
