from ts_lyric_analysis.util import remove_punctuation

def test_remove_punctuation_simple():
    assert remove_punctuation("Hello!") == "Hello"

def test_remove_punctuation_none():
    assert remove_punctuation("Hello") == "Hello"

def test_remove_punctuation_middle():
    assert remove_punctuation("h.e.l.l.o") == "hello"

def test_remove_punctuation_numbers():
    assert remove_punctuation("22") == "22"

def test_remove_punctuation_characters():
    assert remove_punctuation("!@#$%^&*()-,./'") == ""
