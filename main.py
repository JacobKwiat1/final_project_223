from Messaging import DM_Session

def main():
    # Send inputted username to server
    valid_signup = False
    valid_login = False
    uname = ""
    passwd = ""
    choice = input("Login(1) or signup?(2): ")

    # Sign-up loop
    if choice == "2":
        while valid_signup == False:
            print("---Sign up---")
            uname = input("Enter your username: ")
            passwd = input("Enter your password: ")
            
            # CREATE ACCOUNT #
            

    # Log-in Loop
    while valid_login == False:
        # Get credentials from user
        print("---Log in---")
        uname = input("Enter your username: ")
        passwd = input("Enter your password: ")

        # Check Credentials

    # Post login menu

if __name__ == "__main__":
    main()