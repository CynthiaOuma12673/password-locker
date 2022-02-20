import random
import string

class User:
    '''
    It creates the user class that generates new instances of the user
    '''
    user_list = []

    def _init_(self,username,password):
        
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
        

    def delete_user(self):
        '''
        it deletes a user who has a saved account
        '''

        User.user_list.remove(self)

        #Class secretdetails

        class Secretdetails():

            '''
            This class is used to come up with new objects of the details a user needs 
            '''

            secretdetails_list = []
            @classmethod
            def confirm_user(cls,username,password):
                '''
                this method confirms if our user is in the user list or not
                '''

                a_user = ''
                for user in User.user_list:
                    if(user.username == username and user.password == password):
                        a_user == user.username
                return a_user

            def _init_(self, name, password, emailaccount):
                '''
                this method will show the user details that need to be saved
                '''

                self.name = name
                self.password = password
                self.account = emailaccount

            def save_credentials(self):
                '''
                this method will store new details to the secretdtails_list
                '''

                Secretdetails.secretdetails_list.append(self)

