import pytest

from ts_lyric_analysis.lyrics import Lyrics
from ts_lyric_analysis.word import Word

@pytest.fixture
def example_lyric():
    """ Returns a lyric object for testing. The lyric file contains the
    following text:
        ```
        This is one line.
        This is another, line.

        This is a new paragraph
        ```
    """
    return Lyrics("testing")

@pytest.fixture
def testing_lyrics_list_repr():
    return ["This (this) [2]", "is (is) [2]",
            "one (one) [0]", "line. (line) [1]",
            "<BREAK>",
            "This (this) [2]", "is (is) [2]",
            "another, (another) [0]", "line. (line) [1]",
            "<BREAK>", "<PARAGRAPH>", "<BREAK>",
            "This (this) [2]", "is (is) [2]", "a (a) [0]",
            "new (new) [0]", "paragraph (paragraph) [0]",
            "<BREAK>"]

def test_setup(example_lyric, testing_lyrics_list_repr):
    # Check the original lyrics are as expected
    assert len(example_lyric.original_lyrics) == len(testing_lyrics_list_repr)
    for i, l in enumerate(example_lyric.original_lyrics):
        assert l.__repr__() == testing_lyrics_list_repr[i]

    # Check the sorted lyrics are as expected
    sorted_testing_removed = [
            "a (a) [0]", "another, (another) [0]", "is (is) [2]",
            "line. (line) [1]", "new (new) [0]", "one (one) [0]",
            "paragraph (paragraph) [0]", "This (this) [2]"
    ]
    assert len(example_lyric.sorted_lyrics) == len(sorted_testing_removed)
    for i, l in enumerate(example_lyric.sorted_lyrics):
        assert l.__repr__() == sorted_testing_removed[i]

def test_match():
    word_1 = Word("This")
    word_2 = Word("this")
    Lyrics.mark_match(word_1, word_2)
    assert word_1.matched_word == word_2
    assert word_2.matched_word == word_1

def test_display_lyrics(example_lyric):
    expected_result = [
        [["This", "is", "one", "line."],
         ["This", "is", "another,", "line."]],
        [["This", "is", "a", "new", "paragraph"]]
    ]
    # Asserting in this form so I can use the original word and save myself
    # a lot of typing.
    for i, paragraph in enumerate(example_lyric.display_lyrics()):
        for j, line in enumerate(paragraph):
            for k, word in enumerate(line):
                assert word.original_word == expected_result[i][j][k]
