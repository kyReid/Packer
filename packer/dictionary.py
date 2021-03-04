#!/usr/bin/env python

import pikepdf
import zipfile2
from tqdm import tqdm


def dictionary_zip(dictionary, zfile):
    """
    dictionary_zip runs a dictionary attack on a password protected zip file given a list of words

    :param dictionary: wordlist
    :type dictionary: string
    :param zfile: password protected zip file
    :type zfile: string
    """
    # initialize the zip file object
    zip_file = zipfile2.ZipFile(zfile)
    # get length of dictionary
    # check file in a listed binary
    word_count = len(list(open(dictionary, "rb")))
    # run attack
    with open(dictionary, "rb") as dictionary:
        # creates a progress bar for length of list
        for word in tqdm(dictionary, total=word_count, unit="word"):
            try:
                zip_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                print(f"Password found: {word.decode().strip()}")
                exit(0)
    print("Password not found, try a different list")


def dictionary_pdf(dictionary, pdf_file):
    """
    dictionary_pdf runs a dictionary attack on a pdf

    :param dictionary: wordlist
    :type dictionary: string
    :param pdf_file: password protected pdf file
    :type pdf_file: string
    """
    # put all words into a list
    wordlist = list(line.strip() for line in open(dictionary))
    # run attack
    for password in tqdm(wordlist, "decrypting PDF"):
        try:
            with pikepdf.open(dictionary, password=password) as pdf:
                # if password found exit loop
                print(f"password found: {password}")
                break
        except pikepdf._qpdf.PasswordError as e:
            # wrong password,  continue loop
            continue
    print("Password not found, try a different list")
