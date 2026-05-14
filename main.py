from Account_manager import Account_manager
from Messaging import DM_Session

social_media = Account_manager()
current_user = "someone"
logged_in = False
program_exit = False
while(not program_exit):
    user = 0
    while(not logged_in and not program_exit):
        already_error = False
        print("\t\t*** SOCIAL MAIN MENU ***\n\n\t1. Sign Up\n\t2. Log In\n\t3. Save and Exit Program\n")
        try:
            user = int(input("Enter menu choice: "))
        except(ValueError):
            user = 0
            already_error = True
            print("Invalid, please input again.\n")        
        if(user == 1):
            username = input("Enter username: ")
            password = input("Enter password: ")
            output = social_media.create_account(username, password)
            if(not output):
                print("Error in creating account.")
            else:
                print("Added: " + username + ", you may log in now.")
        if(user == 2):
            username = input("Enter username: ")
            password = input("Enter password: ")
            output = social_media.verify_login(username, password)
            if(not output):
                print("Error in logging in.")
            else:
                print(f"Logged in as {username}.")
                logged_in = True
                current_user = username
        if(user == 3):
            social_media.save_data()
            program_exit = True
    user = 0
    while(user != 11 and not program_exit):
            already_error = False
            print("\t\t*** SOCIAL MAIN MENU ***\n\n\t1. Change Password\n\t2. Delete Account\n\t3. Direct Messaging\n\t4. Send Friend Request\n\t5. Approve/Decline Friend Request\n\t6. Check Friends\n\t7. Unfriend User\n\t8. Block User\n\t9. Check Block List\n\t10. Unblock User\n\t11. Logout\n")
            try:
                user = int(input("Enter menu choice: "))
            except(ValueError):
                user = 0
                already_error = True
                print("Invalid, please input again.\n")
            # --- Change Password --- #
            if(user == 1):
                username = current_user
                original_password = input("Enter old password: ")
                password = input("Enter new password: ")
                output = social_media.change_password(username, original_password, password)
                if(not output):
                    print("Error in changing password.")
                else:
                    print("Successfully changed password.")
            # --- Delete Account --- #
            if(user == 2):
                username = current_user
                password = input("Enter password: ")
                output = social_media.delete_account(username, password)
                if(not output):
                    print("Error in deleting account.")
                else:
                    print("Deleted: " + username)
                    user = 11
            # --- Direct Messaging --- #
            if(user == 3):
                sender = current_user
                receiver = input("Enter username to send to: ")
                if(social_media.is_account_real(receiver) == False):
                    print("\n**Error: User does not exist.**\n")
                    close = True
                elif(social_media.is_blocked(receiver, sender)):
                    print(f"\n**Cannot direct message user. {receiver} has blocked you.**\n")
                    close = True
                else:
                    close = False
                    dm = DM_Session(sender, receiver)
                    print("Opened direct messaging with " + receiver + " (type '/quit' to exit).")
                    if(social_media.is_blocked(sender, receiver) == True):
                        print("**WARNING: You have blocked this user. They cannot see your messages and they cannot send you messages.")
                while(not close):
                    dm.print_msgs()
                    message = input("Enter message: ")
                    if(message == "/quit"):
                        close = True
                    else:
                        dm.send(message)
            # --- Send Friend Request --- #
            if(user == 4):
                receiver = input("Enter username to send to: ")
                output = social_media.send_request(current_user, receiver)
                if(not output):
                    print("Error in sending friend request.")
                else:
                    print("Friend request sent.")
            # --- Accept/Deny Friend Requests --- #
            if(user == 5):
                if(not social_media.get_requests(current_user)):
                    print("No Requests.")
                    break
                print("--Incoming Friend Requests--")
                for i in social_media.get_requests(current_user):
                    print(f"\t* {i}")
                sender = input("Enter username to approve/decline: ")
                choice = input("Enter choice ('a' for accept, 'd' for decline): ")
                if(choice == "a"):
                    output = social_media.accept_request(current_user, sender)
                    print("Friend request accepted.")                    
                elif(choice == "d"):
                    output = social_media.decline_request(current_user, sender)
                    print("Friend request declined.")
                else:
                    output = False
                if(not output):
                    print("Error in approving/denying friend request.")
            # --- Check Friends list --- #
            if(user == 6):
                print("--Friends List--")
                for i in social_media.get_friends(current_user):
                    print(f"\t* {i}")
            # --- Unfriend User --- #
            if(user == 7):
                receiver = input("Enter username to unfriend: ")
                output = social_media.remove_friend(current_user, receiver)
                if(not output):
                    print("Error in deleting friend.")
                else:
                    print("Friend deleted.")
            # --- Block User --- #
            if(user == 8):
                receiver = input("Enter username to block: ")
                if(not social_media.is_blocked(current_user, receiver)):
                    output = social_media.add_blocked(current_user, receiver)
                if(not output):
                    print("Error in blocking user.")
                else:
                    print("User blocked.")
            # --- Check blocked users list --- #
            if(user == 9):
                print("--Blocked List--")
                for i in social_media.get_blocked(current_user):
                    print(f"\t* {i}")
            # --- Unblock User --- #
            if(user == 10):
                receiver = input("Enter username to unblock: ")
                output = social_media.remove_blocked(current_user, receiver)
                if(not output):
                    print("Error in unblocking user.")
                else:
                    print("User unblocked.")
            # --- Log out --- #
            if(user == 11):
                logged_in = False
            if((user < 1 or user > 11) and not already_error):
                print("Error, not a choice.\n")
