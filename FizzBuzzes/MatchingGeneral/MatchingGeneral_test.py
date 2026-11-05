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
        for i, line in enumerate(filter(lambda a: a != '', received.split('\n')), start=1):
            if (mod3 := (i % 3 == 0)) & (mod5 := (i % 5 == 0)):
                self.assertTrue(line == 'FizzBuzz')
            elif mod3:
                self.assertTrue(line == 'Fizz')
            elif mod5:
                self.assertTrue(line == 'Buzz')
            else:
                self.assertTrue(line == str(i))

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
            for i, line in enumerate(filter(lambda a: a != '', received.split('\n')), start=1):
                if (mod6 := (i % 6 == 0)) & (mod7 := (i % 7 == 0)):
                    self.assertTrue(line == 'BlargHonk')
                elif mod6:
                    self.assertTrue(line == 'Blarg')
                elif mod7:
                    self.assertTrue(line == 'Honk')
                else:
                    self.assertTrue(line == str(i))

    def test_fb_matching_general_2(self):
        output = StringIO()
        with redirect_stdout(output):
            general_match_fizz_buzz(
                n=77,
                d={
                    3:'Pak',
                    7:'Chooie',
                    11:'Unf'
                }
            )
        received = output.getvalue()
        for line in filter(lambda a: a != '', received.split('\n')):
            for i, line in enumerate(filter(lambda a: a != '', received.split('\n')), start=1):
                if (mod3 := (i % 3 == 0)) & (mod7 := (i % 7 == 0)) & (mod11 := (i % 11 == 0)):
                    self.assertTrue(line == 'PakChooieUnf')
                elif mod3 and mod7:
                    self.assertTrue(line == 'PakChooie')
                elif mod7 and mod11:
                    self.assertTrue(line == 'ChooieUnf')
                elif mod11 and mod3:
                    self.assertTrue(line == 'PakUnf')
                elif mod3:
                    self.assertTrue(line == 'Pak')
                elif mod7:
                    self.assertTrue(line == 'Chooie')
                elif mod11:
                    self.assertTrue(line == 'Unf')
                else:
                    self.assertTrue(line == str(i))

if __name__ == "__main__":
    unittest.main()
