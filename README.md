####Small example of how to use UnitTest2 and Mock:

1. *SetUp* creates conditions that are available in each test.
2. *Mock* allows you to mock a call to an object. If you have multiple mocks each mock is passed into the test bottom to top. 

For example:

```
class SimpleTest(unittest.TestCase):
   @patch("foo.bar")
   @patch("bar.foo")
   def test_this_thing(self, mock_bar, mock_foo):
       mock_bar.return_value = "I am bar.foo"
       mock_foo.return_value = "I am foo.bar"
       self.assertTrue(True, True) ## Yes not a very useful test :-)
```

To run tests, cd to root of repo:

```
pip install unittest2
pip install mock
python test.py
```

Magical - yes? :-)
