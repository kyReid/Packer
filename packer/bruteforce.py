#!/usr/bin/env python

import itertools
import string

import pikepdf
import zipfile2
from tqdm import tqdm


def brute_force_combinations(combo_type):
    """
    brute_force_combinations is a combination of all ascii values including lowercase, uppercase, digits and special
    characters

    :param combo_type: value representing combo to use by users
    :type combo_type: int
    :return: ascii combo
    :rtype: string list of combined ascii values
    """
    # single combination
    if combo_type == 1:
        asci = string.ascii_lowercase
    if combo_type == 2:
        asci = string.ascii_uppercase
    if combo_type == 3:
        asci = string.ascii_letters
    if combo_type == 4:
        asci = string.digits
    if combo_type == 5:
        asci = string.punctuation
    # combination of doubles
    if combo_type == 6:
        asci = string.letters
    if combo_type == 7:
        asci = string.ascii_lowercase + string.digits
    if combo_type == 8:
        asci = string.ascii_lowercase + string.punctuation
    if combo_type == 9:
        asci = string.ascii_uppercase + string.digits
    if combo_type == 10:
        asci = string.ascii_uppercase + string.punctuation
    # combination of triples
    if combo_type == 11:
        asci = string.ascii_letters + string.digits
    if combo_type == 12:
        asci = string.ascii_letters + string.punctuation
    if combo_type == 13:
        asci = string.ascii_lowercase + string.digits + string.punctuation
    if combo_type == 14:
        asci = string.ascii_uppercase + string.digits + string.punctuation
    # combo of all four
    if combo_type == 15:
        asci = string.ascii_letters + string.digits + string.punctuation

    return asci


def brute_force_zip(plock_file, password_length, asci):
    """
    function uses brute-force techniques to gain access to password protected zip files

    :param plock_file: file with password protection
    :param password_length: possible length of password
    :param asci: string combination of ascii values
    """
    # initialize the Zipfile object
    zfile = zipfile2.ZipFile(plock_file)
    # iterates through all asci values and generates a progress bar showing completion process
    for i in tqdm(range(1, (password_length + 1))):
        for letter in itertools.product(asci, repeat=i):
            password = ''.join(letter)
            # if password is proper zip file password, will display, else continue
            try:
                zfile.extractall(pwd=password)
                print('Password found: {}'.format(password))
            except:
                pass

    print("Password not found")


def brute_force_pdf(plock_file, password_length, asci):
    """
    function uses brute-force techniques to gain access to password protected pdf files
    :param plock_file: file with password protection
    :param password_length: possible length of password
    :param asci: string combination of ascii values
    :return:
    """
    # iterates through all asci values and generates a progress bar showing completion process
    for i in tqdm(range(1, (password_length + 1))):
        for letter in itertools.product(asci, repeat=i):
            password = ''.join(letter)
            # uses pikepdf to try and open password protected pdf file using brute force method
            try:
                with pikepdf.open(plock_file, password=password):
                    print(f"Password found: {password}")
                    break
            except pikepdf._qpdf.PasswordError as e:
                # if password fail continue
                continue
