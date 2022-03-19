import pytest
from ts_lyric_analysis.word import Word


EXAMPLE_WORD = "And"
EXAMPLE_WORD_2 = "Between"
EXAMPLE_WORD_FORMATTED = "and"

@pytest.fixture
def word():
    return Word(EXAMPLE_WORD)

@pytest.fixture
def different_word():
    return Word(EXAMPLE_WORD_2)

@pytest.fixture
def different_formatting():
    return Word(EXAMPLE_WORD_FORMATTED)

@pytest.fixture
def line_break():
    return Word(EXAMPLE_WORD, is_line_break=True)

@pytest.fixture
def paragraph_break():
    return Word(EXAMPLE_WORD, is_paragraph_break=True)

def test_init_normal_word(word):
    assert not word.is_line_break
    assert not word.is_paragraph_break
    assert word.original_word == EXAMPLE_WORD
    assert word.formatted_word == EXAMPLE_WORD_FORMATTED

def test_init_line_break(line_break):
    assert line_break.is_line_break
    assert not line_break.is_paragraph_break
    assert line_break.original_word == ""
    assert line_break.formatted_word == ""

def test_init_paragraph_break(paragraph_break):
    assert not paragraph_break.is_line_break
    assert paragraph_break.is_paragraph_break
    assert paragraph_break.original_word == ""
    assert paragraph_break.formatted_word == ""

def test_repr(word, line_break, paragraph_break):
    assert (word.__repr__() 
            == f"{EXAMPLE_WORD} ({EXAMPLE_WORD_FORMATTED}) [0]")
    assert line_break.__repr__() == "<BREAK>"
    assert paragraph_break.__repr__() == "<PARAGRAPH>"

def test_eq_identical(word):
    word2 = Word(EXAMPLE_WORD)
    assert word == word2

def test_eq_diff_format(word):
    word2 = Word(EXAMPLE_WORD_FORMATTED)
    assert word == word2

def test_eq_different(word, different_word):
    assert word != different_word

def test_comparisons_simple(word, different_word):
    assert word < different_word
    assert different_word > word

def test_comparisons_identical(word):
    word_2 = Word(EXAMPLE_WORD)
    assert not word < word_2
    assert not word_2 > word

def test_comparisons_format(word, different_formatting):
    assert not word < different_formatting
    assert not different_formatting > word

def test_add_duplicate(word, different_formatting):
    word.add_duplicate(different_formatting)
    assert len(word.duplicates) == 1
    assert word.duplicates[0] == different_formatting
    assert word.parent is None

    assert len(different_formatting.duplicates) == 0
    assert different_formatting.parent == word

def test_count_duplicates(word, different_formatting):
    word.add_duplicate(different_formatting)
    assert word.count_duplicates() == 1
    assert different_formatting.count_duplicates() == 1

def test_mark_match(word, different_formatting):
    word.mark_match(different_formatting)
    assert word.matched == different_formatting

def test_mark_match_with_dup(word, different_word, different_formatting):
    word.add_duplicate(different_formatting)
    word.mark_match(different_word)
    assert word.matched == different_word
    assert different_formatting.matched == different_word
