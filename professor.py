import random
import sys


# HELLO


def main():
    level = get_level()
    i = 0
    score = 0
    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        expression = f"{x} + {y} = "
        attempt = 0
        while attempt < 3:
            try:
                answer = int(input(expression))
            except ValueError:
                pass
            else:
                if answer != z:
                    print("EEE")
                    attempt += 1
                elif answer == z:
                    i += 1
                    score += 1
                    break
                else:
                    pass
            if attempt == 3:
                print(f"{x} + {y} = {z}")
                i += 1
            else:
                pass
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                return level
            else:
                pass


def generate_integer(level):
    if level == 1:
        r = random.randint(0, 9)
        return r
    elif level == 2:
        r = random.randint(10, 99)
        return r
    elif level == 3:
        r = random.randint(100, 999)
        return r


if __name__ == "__main__":
    main()



