
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def moviepicker(value):
    value_int = int(value)

    if value_int in range(1, 4):
        print('You will be watching: Lord of the Rings: The Fellowship of the Ring')
    elif value_int in range(4, 7):
        print('You will be watching: Lord of the Rings: The Two Towers')
    else:
        if value_int in range(7, 11):
            print('You will be watching: Lord of the Rings: The Return of the King')
        else:
            print('I said ONE through TEN')


value = input('Enter a number between 1 and 10: ')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    moviepicker(value)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
