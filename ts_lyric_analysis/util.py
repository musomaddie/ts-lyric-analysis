import string

def remove_punctuation(s):
    """ Removes all punctuation characters from the given string. This includes
    not just characters at the end of the string, but any punctuation in the
    middle as well. """
    return s.translate(str.maketrans({p: None for p in string.punctuation}))

def make_title_into_filename(title):
    """ Takes a title of a song and makes it into a filename. This (currently)
    involves making it all lowercase and removing any punctuation no matter
    where in the title it is. 
    """
    return remove_punctuation(title.lower())

