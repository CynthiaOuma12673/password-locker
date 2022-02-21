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
