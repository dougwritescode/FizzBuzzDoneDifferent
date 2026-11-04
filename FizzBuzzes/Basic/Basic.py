# Basic FizzBuzz
def FizzBuzz():
    for i in range(1, 16):
        if ((mod3 := (i % 3 == 0)) & (mod5 := (i % 5 == 0))):
            print('FizzBuzz')
        elif mod5:
            print('Buzz')
        elif mod3:
            print('Fizz')
        else:
            print(i)


if __name__ == "__main__":
    FizzBuzz()
