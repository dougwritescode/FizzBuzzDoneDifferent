import unittest
from contextlib import redirect_stdout
from io import StringIO

from FuncComp import func_comp_fizz_buzz


class FizzBuzzFuncCompTest(unittest.TestCase):

    def test_fb_func_comp(self):
        output = StringIO()
        with redirect_stdout(output):
            func_comp_fizz_buzz()
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


if __name__ == "__main__":
    unittest.main()
