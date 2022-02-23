import unittest
from user import User
from details import Secretdetails

class TestClass(unittest.TestCase):

    '''
    This test class will define the test cases for the user class
    '''

    def setUp(self):
        
        self.newuser = User()
        
    def test_save_user(self):

        '''
        test if the new uer has been saved to the list of users
        '''

        self.newuser.save_user()
        self.assertEqual(len(User.user_list), 1)

class TestSecretdetails(unittest.TestCase):
    """
    A test class that defines test cases for secret details class
    """ 
    def setUp(self):
        """
        Method that runs before each individual secret details test methods run.
        """
        self.new_secretdetails = Secretdetails()

    def save_secretdetails_test(self):
        """
        test case to test if the object is saved into the secret details list.
        """
        self.new_secretdetails.save_secretdetails()
        self.assertEqual(len(Secretdetails.secretdetails_list),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Secretdetails.secretdetails_list = []

    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple secret details objects to our secret details list
        '''
        self.new_secretdetails.save_secretdetails()
        test_secretdetail = Secretdetails() 
        test_secretdetail.save_secretdetails()
        self.assertEqual(len(Secretdetails.secretdetails_list),2)

    def test_delete_secretdetail(self):
        """
        test method to test if we can remove an account secret details from our secretdetails_list
        """
        self.new_secretdetails.save_secretdetails()
        test_secretdetail = Secretdetails()
        test_secretdetail.save_secretdetails()

        self.new_secretdetails.delete_secretdetails()
        self.assertEqual(len(Secretdetails.secretdetails_list),1)

    def test_display_all_saved_secretdetails(self):
        '''
        method that displays all the secret details that has been saved by the user
        '''

        self.assertEqual(Secretdetails.show_secretdetails(),Secretdetails.secretdetails_list)

if __name__ == "__main__":
    unittest.main()






