"""
Password generator module.
Contains functions for generating secure passwords.
"""
import string
import random

SYMBOLS = "!@#$%&*/"

def generate_password(password_settings):
    characters = ""
    if password_settings["include_uppercase"]:
        characters += string.ascii_uppercase
    if password_settings["include_lowercase"]:
        characters += string.ascii_lowercase
    if password_settings["include_numbers"]:
        characters += string.digits
    if password_settings["include_symbols"]:
        characters += SYMBOLS
    if password_settings["include_spaces"]:
        characters += " "
    return ''.join(random.choice(characters) for _ in range(password_settings["length"]))