users = [{"name": "omar", "password": "123"}, {"name": "ahmed", "password": "456"}]

def validate_user_password():
    count = 0

    while count < 5:
        user = input("Enter username: ")
        matched_user = None

        
        for i in users:
            if i["name"].lower() == user.lower():
                matched_user = i
                break

        if matched_user:
            password = input("Enter password: ")
            if matched_user["password"] == password:
                print("Welcome !!")
                return 
            else:
                print("Invalid username or password")
                count += 1
        else:
            print("User not found")
            count += 1

    print("User account is locked")

validate_user_password()
