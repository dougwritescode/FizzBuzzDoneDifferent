# Generalized function composition FizzBuzz

def general_func_comp_fizz_buzz(
    n: int = 15,
    d: dict[int, str] = {3: 'Fizz', 5: 'Buzz'},
    sortkey: callable = lambda a: a[0],
):
    def fizz_words(n: int, ):
        outwords = ''
        for num, word in sorted(d.items(), key=sortkey):
            if n % num == 0:
                outwords += word
        return outwords

    def fizz_line(n: int, words: str):
        if len(words) == 0:
            return str(i)
        return ''.join(words)

    for i in range(1, n + 1):
        print(fizz_line(i, fizz_words(i)))


if __name__ == "__main__":
    general_func_comp_fizz_buzz()
