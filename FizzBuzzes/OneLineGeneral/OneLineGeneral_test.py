import unittest
from contextlib import redirect_stdout
from io import StringIO

from OneLineGeneral import general_fizz_buzz_one_line


class GeneralFizzBuzzOneLineTest(unittest.TestCase):

    def test_fb_basic_general_base(self):
        output = StringIO()
        with redirect_stdout(output):
            general_fizz_buzz_one_line()
        received = output.getvalue()
        for i, line in enumerate(filter(lambda a: a != '', received.split('\n')), start=1):
            if (mod3 := (i % 3 == 0)) & (mod5 := (i % 5 == 0)):
                self.assertTrue(line == 'FizzBuzz')
            elif mod5:
                self.assertTrue(line == 'Buzz')
            elif mod3:
                self.assertTrue(line == 'Fizz')
            else:
                self.assertTrue(line == str(i))

    def test_fb_basic_general_custom(self):
        output = StringIO()
        with redirect_stdout(output):
            general_fizz_buzz_one_line(N=42, d={6:'Blarg', 7:'Honk'})
        received = output.getvalue()
        for i, line in enumerate(filter(lambda a: a != '', received.split('\n')), start=1):
            if (mod6 := (i % 6 == 0)) & (mod7 := (i % 7 == 0)):
                self.assertTrue(line == 'BlargHonk')
            elif mod7:
                self.assertTrue(line == 'Honk')
            elif mod6:
                self.assertTrue(line == 'Blarg')
            else:
                self.assertTrue(line == str(i))

    def test_fb_basic_general_custom_2(self):
        output = StringIO()
        with redirect_stdout(output):
            general_fizz_buzz_one_line(N=42, d={2:'Pak', 5:'Chooie', 11:'Unf'})
        received = output.getvalue()
        for i, line in enumerate(filter(lambda a: a != '', received.split('\n')), start=1):
            if (mod2 := (i % 2 == 0)) & (mod5 := (i % 5 == 0)) & (mod11 := (i % 11 == 0)):
                self.assertTrue(line == 'PakChooieUnf')
            elif mod11 and mod5:
                self.assertTrue(line == 'ChooieUnf')
            elif mod11 and mod2:
                self.assertTrue(line == 'PakUnf')
            elif mod5 and mod2:
                self.assertTrue(line == 'PakChooie')
            elif mod11:
                self.assertTrue(line == 'Unf')
            elif mod5:
                self.assertTrue(line == 'Chooie')
            elif mod2:
                self.assertTrue(line == 'Pak')
            else:
                self.assertTrue(line == str(i))

if __name__ == "__main__":
    unittest.main()
