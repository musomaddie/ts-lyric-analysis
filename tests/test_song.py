import pytest

from ts_lyric_analysis.song import Song

@pytest.fixture
def testing_song():
    """ Uses the same testing file as in test_lyrics containing the following
        text:
            ```
            This is one line.
            This is another, line.

            This is a new paragraph
            ```
    """
    return Song("Testing", "Test", "Example")

@pytest.fixture
def testing_short_song():
    """ Returns a short song consisting of a single line as follows:
        ``` This is a much shorter song. ```

        From this song (this, is, a) all match original testing song
    """
    return Song("Testing Short", "Test", "Example")

def test_setup(testing_song):
    assert testing_song.name == "Testing"
    assert testing_song.album == "Test"
    assert testing_song.lyric_source == "Example"


def test_repr(testing_song):
    assert testing_song.__repr__() == "Testing"

def test_current_word_match_success(testing_song, testing_short_song):
    lyrics_1 = testing_song.lyrics.sorted_lyrics
    lyrics_2 = testing_short_song.lyrics.sorted_lyrics
    Song._check_current_word_match(lyrics_1, lyrics_2, 0, 0)

    print(lyrics_1[0].matched_word)
    print(lyrics_2[0].matched_word)

    assert lyrics_1[0].matched_word == lyrics_2[0]
    # Confirming it hasn't changed any other matches
    assert lyrics_1[1].matched_word is None
    assert lyrics_2[1].matched_word is None

def test_current_word_match_fail(testing_song, testing_short_song):
    lyrics_1 = testing_song.lyrics.sorted_lyrics
    lyrics_2 = testing_short_song.lyrics.sorted_lyrics
    Song._check_current_word_match(lyrics_1, lyrics_2, 1, 0)

    assert lyrics_1[1].matched_word is None
    assert lyrics_2[0].matched_word is None

def test_move_indices_simple():
    index_1, index_2 = Song._move_indices(["A", "B"], ["B", "C"], 0, 0)
    assert index_1 == 1
    assert index_2 == 0

def test_move_indices_simple_second():
    index_1, index_2 = Song._move_indices(["B", "C"], ["A", "B"], 0, 0)
    assert index_1 == 0
    assert index_2 == 1

def test_move_indices_first_finished():
    index_1, index_2 = Song._move_indices(["A", "B"], ["B", "C"], 1, 0)
    assert index_1 == 1
    assert index_2 == 1

def test_move_indices_second_finished():
    index_1, index_2 = Song._move_indices(["A", "B"], ["B", "C"], 0, 1)
    assert index_1 == 1
    assert index_2 == 1

def test_display_lyrics(testing_song):
    assert testing_song.display_lyrics() == [
        [["This", "is", "one", "line."],
         ["This", "is", "another,", "line."]],
        [["This", "is", "a", "new", "paragraph"]]
    ]

def test_compare_songs_by_sorted(testing_song, testing_short_song):
    testing_song.compare_to_song(testing_short_song)
    # Variables for ease
    testing_result = testing_song.lyrics.sorted_lyrics
    short_result = testing_short_song.lyrics.sorted_lyrics

    # This is whole heap of manual asserts until I figure out a better way.
    """
    sorted_testing_removed = [
            "a (a) [0]", "another, (another) [0]", "is (is) [2]",
            "line. (line) [1]", "new (new) [0]", "one (one) [0]",
            "paragraph (paragraph) [0]", "This (this) [2]"
    ]
    sorted_short = [ a, is, much, shorter, song, this ]
    """
    assert testing_result[0].matched_word == short_result[0]  # a
    assert testing_result[1].matched_word is None  # another
    assert testing_result[2].matched_word == short_result[1]  # is
    assert testing_result[3].matched_word is None  # line
    assert testing_result[4].matched_word is None  # new
    assert testing_result[5].matched_word is None  # one
    assert testing_result[6].matched_word is None  # paragraph
    assert testing_result[7].matched_word == short_result[5]  # this

    assert short_result[0].matched_word == testing_result[0]  # a
    assert short_result[1].matched_word == testing_result[2]  # is
    assert short_result[2].matched_word is None  # much
    assert short_result[3].matched_word is None  # shorter
    assert short_result[4].matched_word is None  # song
    assert short_result[5].matched_word == testing_result[7]  # this

def test_compare_songs_original_positions(testing_song, testing_short_song):
    testing_song.compare_to_song(testing_short_song)

    # Variables for ease
    tr = testing_song.lyrics.original_lyrics
    sr = testing_short_song.lyrics.original_lyrics

    assert tr[0].matched_word == sr[0]  # this
    assert tr[1].matched_word == sr[1]  # is
    assert tr[2].matched_word is None  # one
    assert tr[3].matched_word is None  # line
    assert tr[4].matched_word is None  # BREAK
    assert tr[5].matched_word == sr[0]  # this
    assert tr[6].matched_word == sr[1]  # is
    assert tr[7].matched_word is None  # another
    assert tr[8].matched_word is None  # line
    assert tr[9].matched_word is None  # BREAK
    assert tr[10].matched_word is None  # PARAGRAPH
    assert tr[11].matched_word is None  # BREAK
    assert tr[12].matched_word == sr[0]  # this
    assert tr[13].matched_word == sr[1]  # is
    assert tr[14].matched_word is sr[2]  # a
    assert tr[15].matched_word is None  # new
    assert tr[16].matched_word is None  # paragraph
    assert tr[17].matched_word is None  # BREAK

    assert sr[0].matched_word == tr[0]  # this
    assert sr[1].matched_word == tr[1]  # is
    assert sr[2].matched_word == tr[14]  # a
    assert sr[3].matched_word is None  # much
    assert sr[4].matched_word is None  # shorter
    assert sr[5].matched_word is None  # song
    assert sr[6].matched_word is None  # BREAK
