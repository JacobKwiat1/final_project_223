import json
class Account:
    def __init__(self, username, password, friends=[], blocked=[], new=True):
        self.username = username
        self.password = password
        if new:
            self.password = self.hash(password)
        self.friends = friends
        self.blocked = blocked

    def hash(self, text):
        out = text
        return out
    
    def save_to_file(self, file="users.txt"):
        toSave = {'username': self.username, 'password': self.password, 'friends':self.friends, 'blocked': self.blocked}
        with open(file, 'a') as f:
           f.append(json.dump(toSave))

#helper function as part of module but not class
def load_data(dict):
    return Account(dict['username'], dict['password'], dict['friends'], dict['blocked'], False)