# Fizzbuzz using python pattern matching

def general_match_fizz_buzz(
    n: int=15,
    d={3: 'Fizz', 5: 'Buzz'}
):
    for i in range(1, n + 1):
        mods = [(i % x == 0, d[x]) for x in d.keys()]
        line = f'{i} '
        for m in mods:
            match m[0]:
                case True:
                    line += m[1]
                case _:
                    continue
        print(line)


if __name__ == "__main__":
    general_match_fizz_buzz()