from person import Person ## if you import only the module then it's person.Person for the object :-)
from mock import patch
import unittest2 as unittest


class PersonTest(unittest.TestCase):
	def setUp(self): ##inital conditions for your tests!!!
		self.person = Person("Lorena")

	def test_sets_name_properly(self): 
		self.failUnlessEqual(self.person.get_name(), "Lorena")

	def test_age_based_on_name_len_mult_three(self):
		self.assertEqual(self.person.age(), 18)

	@patch('random.randrange')
	def test_randomize_age_based_on_mult_two(self, mock_random):
		mock_random.return_value = 25 
		self.assertEqual(self.person.randomize_age(), 50)

if __name__ == '__main__': ## http://stackoverflow.com/questions/419163/what-does-if-name-main-do 
    unittest.main() ## When import this file into another this code won't run

"""    
Hitchhiker Guide to Python has good information on best practices and 
conventions: http://docs.python-guide.org/en/latest/writing/tests/ 
"""

