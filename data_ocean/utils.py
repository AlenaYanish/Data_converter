"""
Here we are collecting alf functions for cleaning xml records from whitespaces and /
abbreviations, splitting tag.texts and converting strings with date info to datetimes
"""
import binascii
import datetime
import os
import re


# changing to lowercase, deleting 'р.', 'м.', 'с.', 'смт.', 'смт', 'сщ.', 'с/рада.', 'сщ/рада.', /
# 'вул.' from a string
def clean_name(name):
    return re.sub(r'р\.|м\.|с\.|смт\.|сщ\.|с/рада\.|сщ/рада\.|вул\.', "", name.lower()).strip()


# a dictionary for storing all abbreviations and full forms
SHORT_TO_FULL_DICT = {
    'р-н': 'район',
    'р-ну': 'району',
    'вул.': 'вулиця ',
    'бульв.': 'бульвар ',
    'просп.': 'проспект ',
    'пров.': 'провулок ',
    'пл.': 'площа ',
    'обл.': 'область',
    'области': 'області'
}


# changing to lowercase and abbreviations to full forms like 'р-н' to 'район' /
# (see all cases in short_to_full_dict)
def change_to_full_name(name):
    name = name.lower()
    for abbr, full_form in SHORT_TO_FULL_DICT.items():
        name = name.replace(abbr, full_form)
    return name


# extracting the first word
def get_first_word(string):
    return string.split()[0]


# getting all words before slash and changing string to lowercase
def get_lowercase_substring_before_slash(string):
    return string.split('/')[0].lower()


# extracting all words except first
def cut_first_word(string):
    words_after_first = string.split()[1:]
    return " ".join(words_after_first)


# deleting ';' from a string, then converting it to the datetime format 'Y-m-d'
def format_date_to_yymmdd(str_ddmmyy):
    if ';' in str_ddmmyy:
        str_ddmmyy = str_ddmmyy.replace(";", "")
    if '/' in str_ddmmyy:
        str_ddmmyy = str_ddmmyy.replace("/", ".")
    return datetime.datetime.strptime(str_ddmmyy, "%d.%m.%Y").strftime("%Y-%m-%d")


# checking if exists, then converting to string
def convert_to_string_if_exists(value):
    if value:
        return str(value)
    return None


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()
