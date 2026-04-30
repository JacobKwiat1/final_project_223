import stuff

current_user = "someone"
logged_in = False
program_exit = False
while(not program_exit):
    user = 0
    while(not logged_in):
        already_error = False
        print("\t\t*** SOCIAL MAIN MENU\n\n\t1. Sign Up\n\t2. Log In\n\t3. Exit Program\n")
        try:
            user = int(input("Enter menu choice: "))
        except(ValueError):
            user = 0
            already_error = True
            print("Invalid, please input again.\n")        
        if(user == 1):
            username = input("Enter username: ")
            password = input("Enter password: ")
            output = create_account(username, password)
            if(not output):
                print("Error in creating account.")
            else:
                print("Added: " + username + " , you may log in now.")
        if(user == 2):
            username = input("Enter username: ")
            password = input("Enter password: ")
            output = login(username, password)
            if(not output):
                print("Error in logging in.")
            else:
                print("Logged in.")
                logged_in = True
                current_user = username
        if(user == 3):
            program_exit = True
    user = 0
    while(user != 9 and not program_exit):
            already_error = False
            print("\t\t*** SOCIAL MAIN MENU\n\n\t1. Change Password\n\t2. Delete Account\n\t3. Direct Messaging\n\t4. Send Friend Request\n\t5. Approve Friend Request\n\t6. Check Friends\n\t7. Block User\n\t8. Check Block List\n\t9. Logout\n")
            try:
                user = int(input("Enter menu choice: "))
            except(ValueError):
                user = 0
                already_error = True
                print("Invalid, please input again.\n")
            if(user == 1):
                username = current_user
                original_password = input("Enter old password: ")
                password = input("Enter new password: ")
                output = change_password(username, original_password, password)
                if(not output):
                    print("Error in changing password.")
                else:
                    print("Successfully changed password.")
            if(user == 2):
                username = current_user
                password = input("Enter password: ")
                output = delete_account(username, password)
                if(not output):
                    print("Error in deleting account.")
                else:
                    print("Deleted: " + username)
            if(user == 3):
                sender = current_user
                reciever = input("Enter username to send to: ")
                dm = DM_Session(sender, reciever)
                if(dm == None):
                    print("Error opening direct messaging.")
                else:
                    close = False
                print("Opened direct messaging with " + reciever + " (type '/quit' to exit).")
                while(not close):
                    message = input("Enter message: ")
                    if(message == "/quit"):
                        close = True
                    else:
                        output = send(message)
                        if(not output):
                            print("Error sending message.")
            if(user == 4):
                reciever = input("Enter username to send to: ")
                output = send_friend_request(current_user, reciever)
                if(not output):
                    print("Error in sending friend request.")
                else:
                    print("Friend request sent.")
            if(user == 5):
                amount = friend_request_count
                if(amount > 0):
                    print(friend_request_list)
                    sender = input("Enter username to approve: ")
                    approve_friend_request(current_user, sender)
                    if(not output):
                        print("Error in approving/denying friend request.")
                    else:
                        print("Friend request accepted.")
            if(user == 6):
                check_friend(current_user)
            if(user == 7):
                reciever = input("Enter username to block: ")
                output = block_user(current_user, reciever)
                if(not output):
                    print("Error in blocking user.")
                else:
                    print("User blocked.")
                if(user == 8):
                    check_blocked(current_user)
                if(user == 9):
                    logged_in = False
            if((user < 1 or user > 9) and not already_error):
                print("Error, not a choice.\n")