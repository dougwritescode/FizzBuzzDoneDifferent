# FizzBuzz generalized in one line
general_fizz_buzz_one_line = lambda N = 15, d = {3: 'Fizz', 5: 'Buzz'}: print('\n'.join([f"{i} {''.join(d[k] for k in filter(lambda a: i % a == 0, d.keys()))}" for i in range(1, N + 1)]))

if __name__ == "__main__":
    general_fizz_buzz_one_line()