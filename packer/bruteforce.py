#!/usr/bin/env python

import pikepdf
from tqdm import tqdm
import zipfile2
import itertools
import string


def brute_force_combinations(combo_type):
    """
    brute_force_combinations is a combination of all ascii values including lowercase, uppercase, digits and special characters

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
    # qcombo of all four
    if combo_type == 15:
        asci = string.ascii_letters + string.digits + string.punctuation

    return asci


def brute_force_zip(plock_file, password_length, asci):
    """
    brute_force iterates through asci string list to determine the proper combination of ascii values to crack password

    :param plock_file: file with password protection
    :type plock_file: string
    :param password_length: possible length of password 
    :type password_length: int
    :param asci: string combination of ascii values
    :type asci: string
    """
    # initialize the Zipfile object
    zfile = zipfile2.ZipFile(plock_file)
    # iterates through all asci values and generates a progress bar showing completion process
    for i in tqdm(range(1, (password_length+1))):
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

    # iterates through all asci values and generates a progress bar showing completion process
    for i in tqdm(range(1,(password_length+1))):
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
