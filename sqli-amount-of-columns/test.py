import argparse
import time
from colorama import Fore, Style


class BinSearch:
    __amount = 0
    __guess = 0

    def __init__(self, amount, guess):
        self.__amount = amount
        self.__guess = guess

    def binary_search(self) -> int:
        previous = self.__amount
        current_value = self.__amount % 2 + int(self.__amount / 2)
        while True:
            time.sleep(0.5)
            print(Fore.BLUE, f'[*] Current value:{current_value} Guess: {self.__guess} Previous: {previous}',
                  Style.RESET_ALL)
            additional_arg = current_value % 2
            if current_value == self.__guess:
                print(Fore.GREEN, '[*] Found!')
                return self.__guess

            elif current_value < self.__guess:
                ''' Incresing '''
                tmp_previous = current_value
                current_value = int(abs(previous - current_value) / 2) + additional_arg + current_value
                previous = tmp_previous

            else:
                ''' Decresing '''
                tmp_previous = current_value
                current_value -= int(abs(previous - current_value) / 2) + additional_arg
                previous = tmp_previous


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Finding amount of columns.')
    parser.add_argument('--amount', '-a', nargs=1, type=int, help='Privide a number')
    parser.add_argument('--guess', '-g', nargs=1, type=int, help='Provide a number.')
    args = parser.parse_args()
    print(args)
    bs = BinSearch(args.amount[0], args.guess[0])
    bs.binary_search()
