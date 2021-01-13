import unittest
import file1

class TestFile(unittest.TestCase):
    """ test for file """

    def test_length(self):
        self.assertEqual(file1.length(['hi','w','e']), 3)

if __name__ == '__main__':
    unittest.main()