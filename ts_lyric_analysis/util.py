import string

def remove_punctuation(s):
    return s.translate(str.maketrans({p: None for p in string.punctuation}))
