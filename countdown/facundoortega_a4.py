# Question 1: Repetition allows the code to execute a section of code multiple times. It will keep looping
# until the argument is true. This can allow us to make a code that can check many arguments, which opens the door to
# more complex programs. For example this program runs a repeatable until n is 0 or less than zero


def countdown():
    n = 10000  # file contains descending numbers beginning at 10,000
    print(n)  # had to print the first number because my list began at 9000 from the code in the equation
    while n > 0:  # added this so the code did not run if given a negative number
        for i in range(91):  # used this range since hw_output reset the pattern at i = 90
            n = n - (100 - i)  # noticed that the step that is on is equal to i in the range
            if n >= 0:  # code no longer prints numbers less than 0 it will instead print n and repeats
                print(n)


if __name__ == '__main__':
    countdown()
