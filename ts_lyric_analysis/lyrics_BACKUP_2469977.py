from ts_lyric_analysis.util import make_title_into_filename
from ts_lyric_analysis.word import Word

class Lyrics:

    """
<<<<<<< HEAD
    So this is going to contain all the lyrics in order as they are in the
    song.
=======
    So this is going to contain all the lyrics in order as they are in the song.
>>>>>>> displaying_lyrics
    I need some way to maintain line endings as this is an important thing - so
    this can probably be its own word as a special thing.

    I would like the analysis to run fast so I will need to sort the lyrics to
    allow faster matching - helper function maybe??
<<<<<<< HEAD
        - order to get the comparison and then when reordering count how many
        in the row.
=======
        - order to get the comparison and then when reordering count how many in
          the row.
>>>>>>> displaying_lyrics

    Parameters:
        original_lyrics (list<Word>): all the lyrics in their original
            order, including line breaks
        sorted_lyrics (list<Word>): the lyrics in their sorted order for faster
            matching, all line breaks removed.

    Methods:
        __init__(str): creates a new lyric from the given song name
    """

    def __init__(self, songname):
        """ Creates a new lyric object from the provided song name. This
        involves opening the lyric file and sorting the words so that they can
        be matched.

        Parameters:
            songname (str): the name of the song these lyrics will belong to.
        """
        # Set the default values of everything I need
        self.original_lyrics = []
        self.sorted_lyrics = []

        # Open the lyrics file and set the starting lyric
        self._open_lyrics_file(songname)

    def _find_middle(starting_index, ending_index):
        """ Returns the middle value of these two (i.e. the average) """
        return (starting_index + ending_index) // 2

    def _merge_both_lists(left_list, right_list):
        """ Helper function for the custom sort that takes two lists and merges
        them in sorted order. Takes O(n) time and returns the new merged list.
        """
        combined_list = []
        index_left, index_right = 0, 0
        while True:

            # Special case for empty lists due to not counting the breaks
            if len(left_list) == 0 and len(right_list) == 0:
                return []
            elif len(left_list) == 0:
                return right_list
            elif len(right_list) == 0:
                return left_list

            if (index_left == len(left_list)
                    and index_right == len(right_list)):
                return combined_list

            elif index_left == len(left_list):
                combined_list.append(right_list[index_right])
                index_right += 1
            elif index_right == len(right_list):
                combined_list.append(left_list[index_left])
                index_left += 1

            elif left_list[index_left] < right_list[index_right]:
                combined_list.append(left_list[index_left])
                index_left += 1
            else:
                combined_list.append(right_list[index_right])
                index_right += 1

    def _recursive_custom_sort(original_array, starting_index, ending_index):
        """ Recursive helper function for my custom merge sort. """
        if starting_index == ending_index - 1:
            # Only add to list if this is a word.
            if (original_array[starting_index].is_line_break
                    or original_array[starting_index].is_paragraph_break):
                return []
            return [original_array[starting_index]]
        splitting_index = Lyrics._find_middle(starting_index, ending_index)

        # Now I actually have to do the sort part
        return Lyrics._merge_both_lists(
            Lyrics._recursive_custom_sort(
                original_array, starting_index, splitting_index),
            Lyrics._recursive_custom_sort(
                original_array, splitting_index, ending_index))

    def _open_lyrics_file(self, songname):
        """ Opens the lyric file associated with the song and saves the lyrics
        as a list of lines. All lyric files are saved in the same place with
        the filename following the same convention: static/lyrics/NAME.txt
        where NAME is the song name in lower case without punctuation.

<<<<<<< HEAD
        Parameters:
            songname (str): the name of the song for the lyric file.
=======
            Parameters:
                songname (str): the name of the song for the lyric file.
>>>>>>> displaying_lyrics
        """
        songname_formatted = make_title_into_filename(songname.lower())

        lines = []
<<<<<<< HEAD
        with open(f"ts_lyric_analysis/static/lyrics/{songname_formatted}.txt",
                  "r") as f:
            lines = [line.rstrip() for line in f]
=======
        with open(f"ts_lyric_analysis/static/lyrics/{songname_formatted}.txt", "r") as f:
            lines = [line.strip() for line in f]
>>>>>>> displaying_lyrics
        self._save_lyrics(lines)

    def _save_lyrics(self, lyrics):
        """ From the list of lines provided saves the lyrics as a list of words
        in their original order.

        Parameters:
            lyrics (list<str>): the list of lines that make up the lyrics.
        """
        for lyric in lyrics:
            for word in lyric.split(" "):
                if word == "<PARAGRAPH>":
                    self.original_lyrics.append(
                            Word("", is_paragraph_break=True))
                    continue
                self.original_lyrics.append(Word(word))
            self.original_lyrics.append(Word("", is_line_break=True))
        self._sort_lyrics()

    def _sort_lyrics(self):
        """ Once the original lyrics are created sorts them into order. This
        also involves squishing duplicates into one item and removing line
        breaks.
        """
        # Using sorted(list) hasn't worked because it copies to make the new
        # list therefore changes to the lyrics in sorted_list won't change
        # original. I can't use sort in the original list as I need to
        # maintain it.
        self.sorted_lyrics = Word.remove_duplicates(
                Lyrics._recursive_custom_sort(
                    self.original_lyrics, 0, len(self.original_lyrics)))

    def mark_match(word1, word2):
        """ Marks the two given words as a match for each other.

        Parameters:
            word1: the word from first lyrics to mark as a match
            word2: the word from the second lyrics to mark as a match
        """
        print(f"Match between {word1} and {word2}")
        word1.mark_match(word2)
        word2.mark_match(word1)

    def display_lyrics(self):
        """ Returns the lyrics from this song formatted for display.

        TODO: once db is merged in update this description and the position in the class.
        """
        to_display = []
        current_paragraph = []
        current_line = []
        for word in self.original_lyrics:
            if word.is_line_break:
                # Special case for if the break is right after a paragraph
                if len(current_line) == 0:
                    continue

                current_paragraph.append(current_line)
                current_line = []

            elif word.is_paragraph_break:
                to_display.append(current_paragraph)
                current_line = []
                current_paragraph = []

            else:
                current_line.append(word.original_word)

        # Adding the paragraph to the display as the line has been adding to
        # the paragraph due to the very last line break in the file.
        to_display.append(current_paragraph)
        return to_display
