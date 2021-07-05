#CryptoQuail PasswordCheck
"""Checks a password's strength.
A good password strength is 65
"""

import string as string_
from cryptoquail.util import weak_passwords

global weak
weak = week_passwords.weak_password_database

def check_password(password):
    """checks a password
a good password score is above 65
    """
    score = 0
    score += len(password)
    requirements = {"letters": False, "numbers": False, "symbols": False}
    a = []
    a.extend(list(string_.ascii_letters))
    a.extend(list(string_.digits))
    a.extend(list(string_.punctuation))
    a.append(" ")
    if password in weak:
        return 0
    for char in password:
        if char in a:
            for i in string_.digits:
                if char == i:
                    score += 1
                    requirements["numbers"] = True 
            for i in string_.ascii_letters:
                if char == i:
                    score += 2
                    requirements["letters"] = True
            for i in string_.punctuation:
                if char == i:
                    score += 3
                    requirements["symbols"] = True
        else:
            raise TypeError("unreadable characters")
    score += len(tuple(frozenset(password)))
    if requirements["numbers"] == True: score += 4
    if requirements["letters"] == True: score += 5
    if requirements["symbols"] == True: score += 6
    if len(frozenset(password)) == 1:
        return 1
    return score
