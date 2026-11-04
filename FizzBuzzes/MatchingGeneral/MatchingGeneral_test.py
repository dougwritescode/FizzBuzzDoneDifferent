import unittest
from contextlib import redirect_stdout
from io import StringIO

from MatchingGeneral import general_match_fizz_buzz


class FizzBuzzMatchingTest(unittest.TestCase):

    def test_fb_matching_basic(self):
        output = StringIO()
        with redirect_stdout(output):
            general_match_fizz_buzz()
        received = output.getvalue()
        for line in filter(lambda a: a != '', received.split('\n')):
            splitline = line.split(' ')
            num = int(splitline[0])
            if len(splitline) > 1 and splitline[1] != '':
                self.assertTrue(num % 5 == 0 or num % 3 == 0)
                word = splitline[1]
                if num % 5 == 0 and num % 3 == 0:
                    self.assertTrue(word == 'FizzBuzz')
                elif num % 5 == 0:
                    self.assertTrue(word == 'Buzz')
                elif num % 3 == 0:
                    self.assertTrue(word == 'Fizz')
            else:
                self.assertFalse(num % 5 == 0 or num % 3 == 0)

    def test_fb_matching_general(self):
        output = StringIO()
        with redirect_stdout(output):
            general_match_fizz_buzz(
                n=42,
                d={
                    6: 'Blarg',
                    7: 'Honk'
                }
            )
        received = output.getvalue()
        for line in filter(lambda a: a != '', received.split('\n')):
            splitline = line.split(' ')
            num = int(splitline[0])
            if len(splitline) > 1 and splitline[1] != '':
                self.assertTrue(num % 7 == 0 or num % 6 == 0)
                word = splitline[1]
                if num % 7 == 0 and num % 6 == 0:
                    self.assertTrue(word == 'BlargHonk')
                elif num % 7 == 0:
                    self.assertTrue(word == 'Honk')
                elif num % 6 == 0:
                    self.assertTrue(word == 'Blarg')
            else:
                self.assertFalse(num % 7 == 0 or num % 6 == 0)



if __name__ == "__main__":
    unittest.main()
