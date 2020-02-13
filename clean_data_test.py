import unittest
import clean_data

class TestMyModule(unittest.TestCase):

    def setUP(self):
       return

    def test_to_clean_data(self):
       input_str = "I love you  ✊✊"
       filename = '/Users/yankang/Downloads/glove.twitter.27B/glove.twitter.27B.25d.txt'

       result = clean_data.Preprocess(input_str, filename).indextext
       expected_result = [[10, 68, 15, 4375, 4375, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

       self.assertEqual(result, expected_result)