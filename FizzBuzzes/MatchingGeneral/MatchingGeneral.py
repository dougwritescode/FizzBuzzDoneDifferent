# Fizzbuzz using python pattern matching

def general_match_fizz_buzz(
    n: int=15,
    d={3: 'Fizz', 5: 'Buzz'}
):
    for i in range(1, n + 1):
        mods = list(filter(
            lambda a: a is not None,
            [(i % x == 0, d[x]) if i % x == 0 else None for x in d.keys()]
        ))
        if len(mods) == 0:
            line = str(i)
        else:
            line = ''
            for m in mods:
                match m[0]:
                    case True:
                        line += str(m[1])
                    case _:
                        continue
        print(line)


if __name__ == "__main__":
    general_match_fizz_buzz()
