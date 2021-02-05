#!/usr/bin/env python

import argparse
from stringcolor import *


def get_args():
    parser = argparse.ArgumentParser(description="Packer, a password cracking tool",
                                     epilog="example: pipenv run python3 test.py filename.zip -d wordlist.txt")
    parser.add_argument(
        'plock_file', help='password protected file to crack, must be pdf or zipfile')
    # options for brute force attack
    parser.add_argument('-b', '--brute', default=False, action='store_true',
                        help='a flag for using brute force techniques')
    parser.add_argument('-c', dest='combo_type', type=int, help="1:lowercase 2:uppercase 3:letters 4:digits 5:specials 6:letters 7:lower digits 8:lower specials 9:upper digits 10:upper specials 11:letters digits 12:letters specials 13:lower digits specials 14:upper digits specials 15:letters digits specials")
    parser.add_argument('-pl', dest='password_length',
                        type=int, help='length of password to brute force')

    # options for dictionary attack
    parser.add_argument('-d', '--dict', default=False, action='store_true',
                        help='a flag for using a dictionary attack')
    parser.add_argument('-w', dest='wordlist',
                        help='a file containing a list of words to use in dictionary attack')

    args = parser.parse_args()

    # validate file input is a PDF or Zip file
    if not args.plock_file.lower().endswith(('.zip', '.pdf')):
        parser.error(cs('File must be a PDF or ZIP file', "#ff0009").bold())
    # validate that wordlist is a txt file
    if args.wordlist is not None:
        if '.txt' not in args.wordlist:
            parser.error(cs('Wordlist must be a txt file', "#ff0009").bold())

    return args
