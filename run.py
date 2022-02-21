from user import User, Secretdetails

def function():
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
function()

def create_newuser(username, password):
    '''
    this is function that is used to create a new username and a password
    '''

    newuser = User(username, password)
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

def create_new_secretdetails(emailaccount,name,password):
    '''
    this function will create new secretetails for a new user emailaccount
    '''

    new_secretdetails = Secretdetails(emailaccount,name,password)
    return new_secretdetails

def save_secretdetails(secretetails):
    '''
    this is a function that saves the secret details to the list
    '''

    secretetails.save_secretdetails()

def show_emailaccount_details():
    '''
    this is a function that gives all the saves secret details
    '''

    return Secretetails.show_secretdetails()

def delete_secretdetails(secretetails):
    '''
    this function deletes secretdetails from the secretdetails list
    '''

    secretetails.delete_secretdetails()

def get_secretdetails(emailaccount):
    '''
    this is a function that searches for the secretdetails using the name and password and shows it
    '''

    return Secretdetails.get_secretdetails(emailaccount)

def verify_secretdetails(emailaccount):
    '''
    this function will check if the secret details exist and return a yes or a no
    '''

    return Secretdetails.if_secretdetails_exist(emailaccount)

def obtain_password():
    '''
    this function will create a random password for the user
    '''

    auto_password = Secretdetails.obtainpassword()
    return auto_password


def copy_password(emailaccount):
    '''
    this function will copy the passwrd using pyperclip
    '''

    return Secretdetails.copy_password(emailaccount)

def accessor():
    print('Hae welcome to password locker ...\n Kindly input the following to continue.\n  cn --- Create an account \n  li --- have an account\n')
    short_code = input('').lower().strip()
    if short_code == 'ca':
        print('Sign Up')
        print('*' *50)
        username = input('Username:')
        while True:
            print('tp ---type your password: \n gp ---generate a random password')
            if password_option == 'tp':
                password = input('Input Password\n')
                break
            elif password_option == 'gp':
                password = obtain_password()
                break
            else:
                print('password not correct kindly try again')
        save_user(create_newuser(username, password))
        print('*'*85)
        print(f'Hae {username}, Account successfully created, your password s {password} ')
        print('*'*85)
    elif short_code == 'li':
        print('*'*50)
        print('Input your username and password to login')
        print('*'*50)
        username = input('Username:')
        password = input('password:')
        login = login_user(username, password)
        if login_user == login:
            print(f'Hae {username} welcome to password locker')
            print ('\n')
    while True:
        print('user the following short codes to create your secretdetails\n, cs -- create a new secret details\n ds ---display secretdetails\n fs --find secretdetails\n gp --- obtain random password\n d --- delete details \n ex --- exit the locker\n')
        if short_code == 'cs':
            print('Create new details')
            print('.'*20)
            print('Emailaccount....')
            emailaccount = input().lower()
            print('Your emailaccount name')
            name = input()
            while True:
                print('tp to type your own password if you have an account\n gp --- to obtain a random password')
                password_option = input().lower().strip()
                if password_option == 'tp':
                    password = input('Input your own password\n')
                    break
                else:
                    print('Password is incorrect kindly input again')
                    save_secretdetails(create_new_secretdetails(emailaccount,name,password))
                    print('\n')
                    print(f'emailaccount details for:{emailaccount} - name: {name} - password: {password} has been successfully created')
                    print('\n')
        elif short_code == 'ds':
            if show_emailaccount_details():
                print('Here are your accounts:')
                print('*'*30)
                print('_'*30)
                for emailaccount in show_emailaccount_details():
                    print(f'emailaccount: {emailaccount.emailaccount}\n Name: {username}\n Password: {password}')
                    print('_'*30)
                    print('*'*30)
            else:
                print('You have not created an account')
        elif short_code == 'fs':
            print('Kindly input the email account you wish to serach')
            search_name = input().lower()
            if get_secretdetails(search_name):
                search_secretdetails = get_secretdetails(search_name)
                print(f'emailaccount: {search_secretdetails.name} password : {search_secretdetails.password}')
                print('-'*50)
            else:
                print('The details do not exist')
                print('\n')
        elif short_code == 'd':
            print('enter emailaccount of the details you want to delete')
            search_name = input().lower()
            if get_secretdetails(search_name):
                search_secretdetails = get_secretdetails(search_name)
                print('_'*50)
                search_secretdetails.delete_secretdetails()
                print('\n')
                print(f'your account : {search_secretdetails.emailaccount} has been deleted successfully')
                print('\n')
            else:
                print('The account you want to delete does not exist')
        elif short_code == 'gp':
            password = obtain_password()
            print(f'{password} was successfully obtained')
        elif short_code == 'ex':
            print('Thanks for using password locker, see you next time')
        else:
            print('Kindly input a valid entry')
    else:
        print('Kindly input  valid input to proceed')

    if __name__ == '__main__':
    accessor()





