class User:
    '''
    It creates the user class that generates new instances of the user
    '''
    user_list = []

    def _init_(self,username,password);
        
        '''
        this method will define all the properties that the user needs to have i.e username and password
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        This method will save the new user to the list of users
        '''
        User.user_list.append(self)