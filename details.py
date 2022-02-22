import random
import string
import pyperclip
from user import User
class Secretdetails:

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

            def _init_(self, name, password, account):
                '''
                this method will show the user details that need to be saved
                '''

                self.name = name
                self.password = password
                self.account = account

            def save_secretdetails(self):
                '''
                this method will store new details to the secretdetails_list
                '''

                Secretdetails.secretdetails_list.append(self)

            def delete_secretdetails(self):
                '''
                this method deletes the secretdetails account from the secretdetails list
                '''

                Secretdetails.secretdetails_list.remove(self)

            @classmethod
            def get_secretdetails(cls, account):
                '''
                this method uses the account name to return secret details that are matched to that account
                '''

                for secretdetails in cls.secretdetails_list:
                    if secretdetails.account == account:
                        return secretdetails

            @classmethod
            def copy_password(cls, account):

                '''
                this method checks for the password in the account and allows user access
                '''

                gotten_secretdetails = Secretdetails.get_secretdetails(account)
                pyperclip.copy(gotten_secretdetails.password)

            @classmethod
            def if_secretdetails_exist(cls,account):
                '''
                this method checks if the details exist i the secret details list
                '''

                for secretdetails in cls.secretdetails_list:
                    if secretdetails.account == account:
                        return True
                return False

            @classmethod
            def show_secretdetails(cls):
                '''
                this method will display all the details in the secretdetails list
                '''

                return cls.secretdetails_list
            def obtainpassword(stringLength = 7):
                '''
                this method will generate a strong password with 7characters
                '''

                password = string.ascii_uppercase + string.ascii_lowercase + string.digits + '%&$#@!'
                return ''.join(random.choice(password)for i in range(stringLength))

            


