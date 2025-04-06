# 1. username is not more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter user name: ")

if len(username) > 12:
    print("Username is more than 12 characters")

elif username.find(" ") != -1:
    print("Username cant contain spaces")

elif not username.isalpha():
    print("Usernamecant contain numbers")

else:
    print(f"Welcome {username}")
