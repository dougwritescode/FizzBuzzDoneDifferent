# FizzBuzz in one line
fizz_buzz_one_line = lambda N = 15: print('\n'.join([f'FizzBuzz' if i % 3 == 0 and i % 5 == 0 else f'Fizz' if i % 3 == 0 else f'Buzz' if i % 5 == 0 else str(i) for i in range(1, N + 1)]))

if __name__ == "__main__":
    fizz_buzz_one_line()
