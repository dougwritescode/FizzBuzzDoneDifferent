import unittest
from contextlib import redirect_stdout
from io import StringIO

from OneLineGeneral import general_fizz_buzz_one_line


class GeneralFizzBuzzOneLineTest(unittest.TestCase):

    def test_fb_one_line_general_base(self):
        output = StringIO()
        with redirect_stdout(output):
            general_fizz_buzz_one_line()
        received = output.getvalue()
        for line in filter(lambda a: a != '', received.split('\n')):
            splitline = line.strip().split(' ')
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

    def test_fb_one_line_general_custom(self):
        output = StringIO()
        with redirect_stdout(output):
            general_fizz_buzz_one_line(N=42, d={6:'Blarg', 7:'Honk'})
        received = output.getvalue()
        for line in filter(lambda a: a != '', received.split('\n')):
            splitline = line.strip().split(' ')
            num = int(splitline[0])
            if len(splitline) > 1 and splitline[1] != '':
                self.assertTrue(num % 6 == 0 or num % 7 == 0)
                word = splitline[1]
                if num % 6 == 0 and num % 7 == 0:
                    self.assertTrue(word == 'BlargHonk')
                elif num % 6 == 0:
                    self.assertTrue(word == 'Blarg')
                elif num % 7 == 0:
                    self.assertTrue(word == 'Honk')
            else:
                self.assertFalse(num % 6 == 0 or num % 7 == 0)

if __name__ == "__main__":
    unittest.main()
