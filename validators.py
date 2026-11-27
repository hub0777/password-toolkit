""" Input validation using REGular EXPression """
import re

def is_whole_number(text):
    """ Returns True if the text only contains digits (e.g 12) otherwise False! """
    if re.fullmatch(r"\d+", text):
        return True
    return False