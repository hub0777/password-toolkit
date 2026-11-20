import hashlib
import requests


def check_breach(password):
    """Check if a password appears in known data breaches using the HIBP API.

    Only the first 5 characters of the password's SHA-1 hash are sent,
    so the real password never leaves this computer.
    """
    # Turn the password into a SHA-1 hash, e.g. "password" -> "5BAA61E4..."
    hashed = hashlib.sha1(password.encode()).hexdigest().upper() # converts password to bytes, then hashes it with SHA-1, then converts to uppercase 
    prefix = hashed[0:5]    # first 5 characters, sent to the API
    suffix = hashed[5:]    # the rest, kept on this computer for security

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url, timeout=5) 
        response.raise_for_status()    # raises an error if the API answers with a failure code
    except requests.exceptions.RequestException as e:
        print(f"Could not reach the breach API: {e}") # Incase API call fails, print error and return
        return

    # Each line looks like "SUFFIX:COUNT"
    lines = response.text.splitlines()
    for line in lines:
        line_suffix, count = line.split(":")
        if line_suffix == suffix:
            print(f"WARNING: This password has been seen in {count} known breaches!") 
            print("Do not use it AND change it IMMEDIATELY.")
            return

    print("Good news: this password was not found in any known breach.")