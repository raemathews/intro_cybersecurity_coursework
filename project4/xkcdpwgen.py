#!/usr/bin/env python3

import argparse
import random

HELP_MESSAGE = ("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n\n" +             
"Generate a secure, memorable password using the XKCD method\n\n" +           
"optional arguments:\n" +
"    -h, --help            show this help message and exit\n" +
"    -w WORDS, --words WORDS\n" +
"                         include WORDS words in the password (default=4)\n" +
"    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words\n" +
"                          (default=0)\n" +
"    -n NUMBERS, --numbers NUMBERS\n" +
"                          insert NUMBERS random numbers in the password\n" +
"                          (default=0)\n" +
"    -s SYMBOLS, --symbols SYMBOLS\n" +
"                          insert SYMBOLS random symbols in the password\n" +
"                          (default=0)\n")
parser = argparse.ArgumentParser(usage=HELP_MESSAGE)
parser.add_argument("-w", "--words", help="inlcude WORDS words in the password (default=4)")
parser.add_argument("-c", "--caps", help="capitalize the first letter of CAPS random words (default=0)")
parser.add_argument("-n", "--numbers", help="insert NUMBERS random numbers in the password (deault=0)")
parser.add_argument("-s", "--symbols", help="insert SYMBOLS random symbols in the password (default=0)")
args = parser.parse_args()

WORDS = args.words if args.words != None else 4
CAPS = args.caps if args.caps != None else 0
NUMBERS = args.numbers if args.numbers != None else 0
SYMBOLS = args.symbols if args.symbols != None else 0

def main(num_words, num_caps, num_numbers, num_symbols):
    word_list = get_n_random_words(int(num_words))
    symbol_list = get_n_random_symbols(int(num_symbols))
    digit_list = get_n_random_digits(int(num_numbers))
    word_list_final = word_list_with_caps(word_list, int(num_caps))
    all_elements = word_list_final + symbol_list + digit_list
    random.shuffle(all_elements)
    final_pass = ''.join(all_elements)
    print(final_pass)
    return final_pass


def get_n_random_words(n):
    words = []
    for i in range(n):
        available_words = open('words.txt').read().splitlines()
        word = random.choice(available_words)
        words.append(word)
    return words

def get_n_random_symbols(n):
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "~", ".", ":", ";"]
    return_symbols = []
    for i in range(n):
        symbol = random.choice(symbols)
        return_symbols.append(symbol)
    return return_symbols

def get_n_random_digits(n):
    digits = []
    for i in range (n):
        number = random.randint(0, 9)
        digits.append(str(number))
    return digits

def word_list_with_caps(word_list, num_caps):
    if num_caps > len(word_list):
        num_caps = len(word_list)
    for i in range(num_caps):
        word_list[i] = word_list[i].capitalize()
    return word_list

if __name__ == '__main__':
    main(WORDS, CAPS, NUMBERS, SYMBOLS)



