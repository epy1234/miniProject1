import unittest
import check
import check_words



class MyTestCase(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(check_words.word_count(),3)

if __name__ == '__main__':
    unittest.main()
