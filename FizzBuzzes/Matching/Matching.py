# Fizzbuzz using python pattern matching

def match_fizz_buzz(n: int = 15):
    for i in range(1, n + 1):
        match (i % 3, i %5):
            case (0, 0):
                print(f'FizzBuzz')
            case (0, _):
                print(f'Fizz')
            case (_, 0):
                print(f'Buzz')
            case _:
                print(f'{i}')


if __name__ == "__main__":
    match_fizz_buzz()
