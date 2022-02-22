from user import User
from details import Secretdetails

def function():
    print("                          __    __   __  ")
    print("                         |  |  |  | |  | ")
    print("                         |  |__|  | |  | ")
    print("                         |   __   | |  | ")
    print("                         |  |  |  | |  | ")
    print("                         |__|  |__| |__| ")
function()

def create_newuser(self,username, password):
    '''
    this is function that is used to create a new username and a password
    '''

    newuser = User(self,username, password)
    return newuser

def save_user(user):
    '''
    this function will save a new user after it is created
    '''

    user.save_user()

def show_user():

    '''
    this is a function that will show the user who is already existing
    '''

    return User.show_user()

def login_user(username,password):
    '''
    a function that lets the user login after checking the details
    '''

    verify_user = Secretdetails.confirm_user(username,password)
    return verify_user

def create_new_secretdetails(account,name,password):
    '''
    this function will create new secretetails for a new user account
    '''

    new_secretdetails = Secretdetails(account,name,password)
    return new_secretdetails

def save_secretdetails(secretetails):
    '''
    this is a function that saves the secret details to the list
    '''

    secretetails.save_secretdetails()

def show_account_details():
    '''
    this is a function that gives all the saves secret details
    '''

    return Secretetails.show_secretdetails()

def delete_secretdetails(secretetails):
    '''
    this function deletes secretdetails from the secretdetails list
    '''

    secretetails.delete_secretdetails()

def get_secretdetails(account):
    '''
    this is a function that searches for the secretdetails using the name and password and shows it
    '''

    return Secretdetails.get_secretdetails(account)

def verify_secretdetails(account):
    '''
    this function will check if the secret details exist and return a yes or a no
    '''

    return Secretdetails.if_secretdetails_exist(account)

def obtain_password():
    '''
    this function will create a random password for the user
    '''

    auto_password = Secretdetails.obtainpassword()
    return auto_password


def copy_password(account):
    '''
    this function will copy the passwrd using pyperclip
    '''

    return Secretdetails.copy_password(account)                 

def main():
    print('Hae welcome to password locker ...\n Kindly input the following to continue.\n  cn --- Create an account \n  li --- have an account\n')
    short_code = input('').lower().strip()
    if short_code == 'cn':
        print('Sign Up')
        username = input('Username:')
        while True:
            print('tp ---type your password: \n gp ---generate a random password')
            password_option = input().lower().strip()
            if password_option == 'tp':
                password = input('Input Password\n')
                print(f"Hae {username}, Your account has been created succesfully! Your password is: {password}")
                return password
                break
            elif password_option == 'gp':
                password = obtain_password()
                print(f"Hae {username}, Your account has been created succesfully! Your password is: {password}")
                return password
                break
            
            else:
                print('password not correct kindly try again')

    elif short_code == 'li':
        print('Input your username and password to login')
        username = input('Username:')
        password = input('password:')
        print ('\n')
        print(f'Hae {username} welcome to password locker')
        print ('\n')
        
    while True:
        print('user the following short codes to create your secretdetails\n cs -- create a new secret details\n ds ---display secretdetails\n fs --find secretdetails\n gp --- obtain random password\n d --- delete details \n ex --- exit the locker\n')
        short_code = input('').lower().strip()
        if short_code == 'cs':
            print('Create new details')
            print('Account name ....')
            account = input().lower()
            print('Your account name')
            name = input()
            while True:
                print('tp ---to type your own password if you have an account\n gp --- to obtain a random password')
                password_option = input().lower().strip()
                if password_option == 'tp':
                    password = input('Input your own password\n')
                    print('\n')
                    print(f'Account details for:{account} - name: {name} - password: {password} has been successfully created')
                    print('\n')
                    break
                else:
                    print('Password is incorrect kindly input again')
                    break
        elif short_code == 'ds':
            if show_account_details():
                print('Here are your accounts:')
                for account in show_account_details():
                    print(f'account: {account.account}\n Name: {username}\n Password: {password}')
                    break
            else:
                print('You have not created an account')
                
        elif short_code == 'fs':
            print('Kindly input the  account you wish to search')
            search_name = input().lower()
            if get_secretdetails(search_name):
                search_secretdetails = get_secretdetails(search_name)
                print(f'account: {search_secretdetails.name} password : {search_secretdetails.password}')
                break
            else:
                print('The details do not exist')
                print('\n')
        elif short_code == 'd':
            print('enter account of the details you want to delete')
            search_name = input().lower()
            if get_secretdetails(search_name):
                search_secretdetails = get_secretdetails(search_name)
                search_secretdetails.delete_secretdetails()
                print('\n')
                print(f'your account : {search_secretdetails.account} has been deleted successfully')
                print('\n')
            else:
                print('The account you want to delete does not exist')
        elif short_code == 'gp':
            password = obtain_password()
            print(f'{password} was successfully obtained')
            break
        elif short_code == 'ex':
            print('Thanks for using password locker, see you next time')
            break
        else:
            print('Kindly input a valid entry')
            break
    else:
        print('Kindly input  valid input to proceed')
        

if __name__ == '__main__':
    main()

        





