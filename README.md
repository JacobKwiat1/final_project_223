# Social Media Lab

## Project Description
This project is a social media platform that allows direct messaging between users. Users can create accounts, and can message users as long as they know their username.
Accounts are stored in the 'account_management.json' file with usernames as the keys, and store users' usernames, hashed passwords, friends lists, blocked lists, and friend requests lists.
Messages are sent via log files, of which there are individual files for each conversation between two users. The message history persists between sessions, and thefile names are based on 
the usernames of the two people messaging eachother. The message logs go into the 'Logs' directory.

## Running the application
1. In the same directory as the 'main.py' file, run 'python3 main.py' for Linux and MAC or 'python main.py' for Windows.
2. All action options are displayed through standard output, enter an integer to select your action.
3. When finished, make sure to logout and then enter 3 in the main menu to save all changes and exit the program.
