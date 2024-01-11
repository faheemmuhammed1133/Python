def signin():
    print("create Account:")
    username = input("Create Useranme:")
    password = input('Create Password:')
    return username,password

def login(username,password):
    print("\nLogin:")
    entered_username = input("Enter Your Username ")
    entered_password = input("Enter Password ")
    
    if entered_username == username and entered_password == password :
        print ("Login succesful 🎯")
    else :
        print("Incorrect username or password. Please try again.💩")
        login(username,password)


def main():
    choice = input("Do you want to create an account? (yes/no): ")
    if choice.lower() == "yes":
            username, password = signin()
    else:
            username = "demo_user"
            password = "demo_pass"

    login(username, password)
if __name__ == "__main__":
     main()
