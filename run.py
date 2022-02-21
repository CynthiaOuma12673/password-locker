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
