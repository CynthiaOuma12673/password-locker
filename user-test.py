import unittest
from user import User

class testuser(unittest.TestCase);
    '''
    This test class will define the test cases for the user class
    '''
    def setUp(self);
        
        self.newuser = User('OumaCynthia', 'Cyn12673#')
