import string

def remove_punctuation(s):
    """ Removes all punctuation characters from the given string. This includes
    not just characters at the end of the string, but any punctuation in the
    middle as well. """
    return s.translate(str.maketrans({p: None for p in string.punctuation}))

