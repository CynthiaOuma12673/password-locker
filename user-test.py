import unittest
from user import User

class testuser(unittest.TestCase);
    '''
    This test class will define the test cases for the user class
    '''
    def setUp(self);
        
        self.newuser = User('OumaCynthia', 'Cyn12673#')

    def test_init(self);
        self.assertEqual(self.newuser.username,'OumaCynthia')
        self.assertEqual(self.newuser.password,'Cyn12673#')

if _name_ == "_main_":
    unittest.main()
