max_attempts = 3
correct_password = "Admin123"

attempts = 0

while attempts < max_attempts:
    password = input("Enter Password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        print("Incorrect Password")

if attempts == max_attempts:
    print("Access Restricted! Too many failed attempts.")