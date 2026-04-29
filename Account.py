class Account:
    def __init__(self, username, password, friends=set(), blocked=set(), new=True):
        self.username = username
        self.password = password
        if new:
            self.password = self.hash(password)
        self.friends = friends
        self.blocked = blocked

    def __repr__(self):
        return f'username={self.username}\npassword={self.password}\nfriends={self.friends}\nblocked={self.blocked}'
    
    def hash(self, text):
        out = text
        return out
    
    def prep_to_save(self):
        return {'username': self.username, 'password': self.password, 'friends':self.friends, 'blocked': self.blocked}
        
    def add_friend(self, user):
        self.friends.append(user)

    def add_blocked(self, user):
        self.blocked.append(user)

    def get_username(self):
        return self.username
    

#helper function as part of module but not class
def load_data(dict):
    return Account(dict['username'], dict['password'], dict['friends'], dict['blocked'], False)