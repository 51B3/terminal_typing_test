import time
import msvcrt
import cutie
import json
import random
from colorama import Back, Fore


def clear():
    print('\x1b[2J', end='\r')


amount = 0
def menu():
    global amount
    amounts = [10, 25, 50, 75, 100]
    clear()
    print('Amount of words:')
    choice = cutie.select(
        amounts,
        deselected_prefix=Fore.LIGHTBLACK_EX + '○ ' + Fore.RESET,
        selected_prefix=Fore.BLUE + '● ' + Fore.RESET
    )
    amount = amounts[choice]
    gen(amount)


def gen(amount):
    with open('words.json', 'r') as file:
        words = json.load(file)

    lst = random.sample(words, amount)
    convert(lst)


text = ''
def convert(lst):
    global text
    current = ''
    rest = ''
    for el in range(1, len(lst)):
        if el % 10 == 0:
            lst[el] += '\n'
        else:
            lst[el] += ' '

    result = ''.join(lst[::-1])
    if len(lst) == 10:
        current = result
    else:
        i = result.rfind('\n')
        current = result[i+1:]
        rest = result[:i]
    
    text = result.replace('\n', ' ')
    output(current, rest)


"""
TODO:
Redesign the WPM counting system
"""


speed = []
typos = 0
def stat():
    global text, speed, typos
    cpm = round((len(text) - typos) / (sum(speed) / 60))
    wpm = round(len(text.split(' ')) / (sum(speed) / 60))
    accuracy = round((len(text) - typos) / len(text) * 100)
    clear()
    print(f'\nCPM: {cpm}\nWPM: {wpm}\naccuracy: {accuracy}%\n')


keyboard = '\n[ 1 ][ 2 ][ 3 ][ 4 ][ 5 ][ 6 ][ 7 ][ 8 ][ 9 ][ 0 ]\
            \n[ Q ][ W ][ E ][ R ][ T ][ Y ][ U ][ I ][ O ][ P ]\
            \n     [ A ][ S ][ D ][ F ][ G ][ H ][ J ][ K ][ L ]\
            \n     [ Z ][ X ][ C ][ V ][ B ][ N ][ M ]\
            \n          [                       ]\n'
keys = {
    6: {'1': '[ 1 ]', '2': '[ 2 ]', '3': '[ 3 ]', '4': '[ 4 ]', '5': '[ 5 ]', '6': '[ 6 ]', '7': '[ 7 ]', '8': '[ 8 ]', '9': '[ 9 ]', '0': '[ 0 ]'},
    5: {'q': '[ Q ]', 'w': '[ W ]', 'e': '[ E ]', 'r': '[ R ]', 't': '[ T ]', 'y': '[ Y ]', 'u': '[ U ]', 'i': '[ I ]', 'o': '[ O ]', 'p': '[ P ]'},
    4: {'a': '     [ A ]', 's': '[ S ]', 'd': '[ D ]', 'f': '[ F ]', 'g': '[ G ]', 'h': '[ H ]', 'j': '[ J ]', 'k': '[ K ]', 'l': '[ L ]'},
    3: {'z': '     [ Z ]', 'x': '[ X ]', 'c': '[ C ]', 'v': '[ V ]', 'b': '[ B ]', 'n': '[ N ]', 'm': '[ M ]'},
    2: {' ': '          [                       ]'}
}
def output(current, rest=None):
    global amount, typos, speed
    str = iter(current)
    input = []
    clear()
    print(Fore.LIGHTBLACK_EX + rest + Fore.RESET)
    print(current, end='\r')
    print('\n' + keyboard, end='\r')
    start = time.time()


    def get(key):
        global typos, keyboard, keys
        nonlocal input
        try:
            char = next(str)
            if key != char:
                typos += 1
                key = Back.RED + char + Back.RESET
            else:
                key = Fore.BLUE + char + Fore.RESET

            input.append(key)
            if len(input) > 1:
                print(f'\033[7A\033[{len(input)-1}C' + input[-1])
            else:
                print(f'\033[7A' + input[-1])

            print(keyboard, end='\r')
        except StopIteration:
            pass

    while True:
        key = msvcrt.getch()
        # CTRL + R
        if key == b'\x12':
            speed = []
            typos = 0
            return gen(amount)

        key = key.decode()
        if key.isprintable():
            get(key)

        for column, row in keys.items():
            if key in row:
                active = ''
                for _, value in row.items():
                    if key == _:
                        active += Fore.BLUE + value + Fore.RESET
                    else:
                        active += value

                print(f'\033[{column}A')
                print(active, end='\r')
                print(f'\033[{column-1}B', end='\r')

        if len(input) == len(current):
            break

    speed.append(time.time() - start)
    if rest != '':
        text = rest.split('\n')
        text = list(filter(None, text))
        current = text[-1]
        rest = ''
        for el in text:
            if el == current:
                continue

            rest += f'\n{el}'

        output(current, rest)
    else:
        stat()


if __name__ == '__main__':
    menu()