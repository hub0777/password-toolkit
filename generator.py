import string
import secrets


def generate_password(length):
    """ Generate a random password of the specified length """
    password_chars = []
    skip = {"0","O","l","I","1"}

    all_chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    for i in skip:
        all_chars.remove(i)
    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))
    password = "".join(password_chars)
    print(password)

