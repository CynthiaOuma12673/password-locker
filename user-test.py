import unittest
from user import User
from details import Secretdetails

class TestClass(unittest.TestCase):

    '''
    This test class will define the test cases for the user class
    '''

    def setUp(self);
        
        self.newuser = User('OumaCynthia', 'Cyn12673#')

    def test_init(self):

        '''
        test if the new  new user object has been intialized well
        '''

        self.assertEqual(self.newuser.username,'OumaCynthia')
        self.assertEqual(self.newuser.password,'Cyn12673#')

    def test_save_user(self):

        '''
        test if the new uer has been saved to the list of users
        '''

        self.newuser.save_user()
        self.assertEqual(len(User.user_list), 1)



if _name_ == "_main_":
    unittest.main()

