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


