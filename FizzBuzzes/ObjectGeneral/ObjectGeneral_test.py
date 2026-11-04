import unittest
from contextlib import redirect_stdout
from io import StringIO

from ObjectGeneral import FizzBuzzObjectGeneral


class GeneralFizzBuzzObjectTest(unittest.TestCase):

    def test_fb_object_general_base(self):
        output = StringIO()
        with redirect_stdout(output):
            FizzBuzzObjectGeneral(
                d={3: 'Fizz', 5: 'Buzz'},
                s=lambda a: a[1]
            )
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

    def test_fb_object_general_custom(self):
        output = StringIO()
        with redirect_stdout(output):
            FizzBuzzObjectGeneral(
                d={6: 'Blarg', 7: 'Honk'},
                s=lambda a: a[1]
            )
        received = output.getvalue()
        for line in filter(lambda a: a != '', received.split('\n')):
            splitline = line.strip().split(' ')
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
                self.assertFalse(num % 5 == 0 or num % 3 == 0)


if __name__ == "__main__":
    unittest.main()
