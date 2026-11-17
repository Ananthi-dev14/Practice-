def login(username, password):
    correct_username = "admin"
    correct_password = "12345"

    if username == correct_username and password == correct_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


# Test the login function
login("admin", "12345")
login("user", "wrong")
