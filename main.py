import time
import json
import cutie
import msvcrt
import random

from colorama import Back, Fore
from keyboard import layout, keys


def clear():
    print('\x1b[2J\x1b[H', end='')


amount = 0
def menu():
    global amount
    amounts = [10, 25, 50, 75, 100]
    clear()
    print(f'{Fore.BLUE}Typing test{Fore.RESET}\n')
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
        list = json.load(file)

    words = random.sample(list, amount)
    convert(words)


text = ''
indent = 0
def convert(words):
    global text, indent
    current = ''
    rest = ''
    for i, _ in enumerate(words, start=1):
        if i == len(words):
            break
        
        if i % 10 == 0:
            words[i-1] += '\n'
        else:
            words[i-1] += ' '

    result = ''.join(words)
    if len(words) == 10:
        current = result
        indent = 1
    else:
        sep = result.find('\n')
        current = result[:sep]
        rest = result[sep:]
        indent = len(result.splitlines())
    
    text = result.replace('\n', ' ')
    draw(current, rest)


speed = []
typos = 0
def stat():
    global speed, typos
    cpm = round((len(text) - typos) / (sum(speed) / 60))
    accuracy = round((len(text) - typos) / len(text) * 100)
    clear()
    print(f'{Fore.BLUE}Statistics:{Fore.RESET}\n')
    print(f'CPM: {cpm}\naccuracy: {accuracy}%\n')
    print(f'{Fore.LIGHTBLACK_EX}↱ Ctrl + M    ☓ Ctrl + C{Fore.RESET}')
    while True:
        sym = msvcrt.getch()
        if sym == b'\x03':
            return
        
        if sym == b'\x0D':
            speed = []
            typos = 0
            menu()
            return
        

def draw(current, rest=None):
    global typos, speed, indent
    line = iter(current)
    input = []
    clear()
    print(current, end='')
    print(Fore.LIGHTBLACK_EX + rest + Fore.RESET)
    print(f'\n{layout}')
    print(f'\n{Fore.LIGHTBLACK_EX}↻ Ctrl + R{Fore.RESET}')
    start = time.time()


    def get(sym):
        global typos
        try:
            char = next(line)
            if sym == char:
                sym = Fore.BLUE + char + Fore.RESET
            else:
                typos += 1
                sym = Back.RED + char + Back.RESET

            input.append(sym)
            print('\x1b[H', end='')
            if len(input) > 1:
                print(f'\x1b[{len(input)-1}C' + input[-1])
            else:
                print('' + input[-1])

        except StopIteration:
            pass


    while True:
        sym = msvcrt.getch()
        if sym == b'\x12':
            speed = []
            typos = 0
            gen(amount)
            return

        sym = sym.decode()
        if sym.isprintable():
            get(sym)

        for column, row in keys.items():
            if sym in row:
                active = ''
                for key, value in row.items():
                    if sym == key:
                        active += Fore.BLUE + value + Fore.RESET
                    else:
                        active += value
                
                print(f'\x1b[{indent}B{layout}')
                print(f'\x1b[{column}A{active}')
                print(f'\x1b[{column-1}B')

        if len(input) == len(current):
            break

    speed.append(time.time() - start)
    if rest != '':
        text = rest.split('\n')
        text = list(filter(None, text))
        current = text[0]
        rest = ''
        for line in text:
            if line == current:
                continue

            rest += f'\n{line}'

        indent = len((current + rest).splitlines())
        draw(current, rest)
    else:
        stat()


if __name__ == '__main__':
    menu()
