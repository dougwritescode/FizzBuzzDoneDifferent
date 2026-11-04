import unittest
from contextlib import redirect_stdout
from io import StringIO

from Basic import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    def test_fb_one_line(self):
        output = StringIO()
        with redirect_stdout(output):
            FizzBuzz()
        received = output.getvalue()
        for i, line in enumerate(filter(lambda a: a != '', received.split('\n')), start=1):
            # Capture modulus tests as vars to not repeat conditions
            if ((mod3 := i % 3 == 0) & (mod5 := i % 5 == 0)):
                self.assertTrue(line == 'FizzBuzz')
            elif mod3:
                self.assertTrue(line == 'Fizz')
            elif mod5:
                self.assertTrue(line == 'Buzz')
            else:
                self.assertTrue(line == str(i))

if __name__ == "__main__":
    unittest.main()
