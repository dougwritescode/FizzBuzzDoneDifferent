# Function composition FizzBuzz


def func_comp_fizz_buzz():

    def fizz_words(n: int, ):
        outwords = ''
        fbwords = {3: 'Fizz', 5: 'Buzz'}
        for num, word in sorted(fbwords.items(), key=lambda a: a[0]):
            if n % num == 0:
                outwords += word
        return outwords

    def fizz_line(n: int, words: str):
        if len(words) == 0:
            return str(n)
        return ''.join(words)

    for i in range(1, 16):
        print(fizz_line(i, fizz_words(i)))


if __name__ == "__main__":
    func_comp_fizz_buzz()
