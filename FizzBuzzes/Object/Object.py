# Object-Oriented FizzBuzz

class FizzBuzzObject(object):
    
    def __init__(self):
        self.d = {3: 'Fizz', 5: 'Buzz'}
        self.s = lambda a: a[0]
        self.i = 1
    
    def __call__(self, n: int = 15):
        temp = self.i
        self.i = 1
        for i in range(1, n + 1):
            yield next(self)
        self.i = temp
    
    def __next__(self):
        outline = f'{self.i} '
        for num, word in sorted(self.d.items(), key=self.s):
            if num == 0:
                continue
            if self.i % num == 0:
                outline += word
        self.i += 1
        return outline


if __name__ == "__main__":
    fbo = FizzBuzzObject()
    for n in fbo():
        print(n)