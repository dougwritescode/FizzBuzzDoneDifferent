# Object-Oriented FizzBuzz
from dataclasses import dataclass

@dataclass
class FizzBuzzObjectGeneral(object):
    d: dict[int, str]
    s: callable

    def __post_init__(self):
        self.i = 1

    def __call__(self, n: int = 15):
        temp = self.i
        self.i = 1
        for i in range(1, n + 1):
            yield next(self)
        self.i = temp

    def __next__(self):
        outline = ''
        for i, (num, word) in enumerate(sorted(self.d.items(), key=self.s), start=1):
            if self.i % num == 0:
                outline += word
            if i == len(self.d.items()) and len(outline) > 0:
                break
        else:
            outline = str(self.i)
        self.i += 1
        return outline


if __name__ == "__main__":
    fbo = FizzBuzzObjectGeneral(
        d={3: 'Fizz', 5: 'Buzz'},
        s=lambda a: a[0]
    )
    for n in fbo():
        print(n)
