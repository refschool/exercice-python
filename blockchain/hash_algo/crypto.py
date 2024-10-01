import hashlib

def hash256(text):

    encoded = text.encode()
    sha = hashlib.sha256(encoded)
    """ get the hex version of the hash """
    hash = sha.hexdigest()
    return hash
