from termcolor import colored
import pyfiglet
import pdb


def color(msg, **kwargs):
    res = pyfiglet.figlet_format(msg)
    return colored(res, color=kwargs.get('color'))


def main():
    try:
        msg = input('What message would you like to see in ascii?: ')
        col = input(
            'What will be the color the message?\n(red, green, yellow, blue, magenta, cyan, white): ').lower()
        v_col = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        while col not in v_col:
            col = input(
                f'{col} is not a valid color!\nHere are the valid colors {v_col}: ')
        return color(msg, color=col)
    except KeyError:
        return 'Please enter a valid message!'


print(main())
