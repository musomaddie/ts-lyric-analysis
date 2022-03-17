from util import remove_punctuation

class Lyrics:

    """ 
    So this is going to contain all the lyrics in order as they are in the song. 
    I need some way to maintain line endings as this is an important thing - so
    this can probably be its own word as a special thing.

    I would like the analysis to run fast so I will need to sort the lyrics to
    allow faster matching - helper function maybe??
        - order to get the comparison and then when reordering count how many in
          the row. 

        Parameters:
            length (int): the number of words (including line breaks as a special
                word) in the song
            original_lyrics (list<Word>): the special word that starts the 
                lyrics in their original order.
            sorted_lyrics (list<Word>): the special word that starts the chain in 
                sorted order.
            matches (list): a list of all words from this song that match a
                different song.

        Methods:
            __init__(str): creates a new lyric from the given songname
    """

    def __init__(self, songname):
        """ Creates a new lyric object from the provided songname. This involves
        opening the lyric file and sorting the words so that they can be
        matched.

            Parameters:
                songname (str): the name of the song these lyrics will belong
                to.
        """
        self.length = 0

        # Set the default values of everything I need
        self.original_lyrics = []
        self.sorted_lyrics = []
        self.matches = [] 

        # Open the lyrics file and set the starting lyric
        self._open_lyrics_file(songname)

    def _open_lyrics_file(self, songname):
        """ Opens the lyric file associated with the song and saves the lyrics
        as a list of lines. All lyric files are saved in the same place with the
        filename following the same convention: static/lyrics/NAME.txt where
        NAME is the song name in lower case without punctuation.

            Parameters: 
                songname (str): the name of the song for the lyric file.
        """
        songname_formatted = remove_punctuation(songname.lower())

        lines = []
        with open(f"static/lyrics/{songname_formatted}.txt", "r") as f:
            lines = [line.rstrip() for line in f]
        self._save_lyrics(lines)

    def _save_lyrics(self, lyrics):
        """ From the list of lines provided saves the lyrics as a list of words
        in their original order.

            Parameters:
                lyrics (list<str>): the list of lines that make up the lyrics.
        """
        pass
