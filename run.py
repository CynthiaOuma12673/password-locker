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
