# FizzBuzz in one line
fizz_buzz_one_line = lambda N = 15: print('\n'.join([f'{i} FizzBuzz' if i % 3 == 0 and i % 5 == 0 else f'{i} Fizz' if i % 3 == 0 else f'{i} Buzz' if i % 5 == 0 else f'{i}' for i in range(1, N + 1)]))

if __name__ == "__main__":
    fizz_buzz_one_line()