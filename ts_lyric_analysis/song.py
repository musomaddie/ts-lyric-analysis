from lyrics import Lyrics

class Song:
    """ Contains all the information needed for the current song.

        Parameters:
            name (string): the name of the song
            album (string): the name of the album the song is on.
            lyrics (Lyrics): the lyrics of the song
            lyric_source (string): the source where there lyrics is from.
    
        Methods:
            __init__(name, album, lyric_source): creates a new Song object using
                the given name, album and lyric source. Assumes that the lyrics
                for the song are saved in an appropriately named file.
            compare_to_song(song): finds all the words in common between this
                song and the supplied one.
    """

    # TODO: write a population script and save all this information in a db so I
    # can look it up easily and not have a bunch of static files floating
    # around.

    # I will leave the lyrics inside a folder to cut down file size.

    def __init__(self, name, album, lyric_source):
        """ Creates an new song object with the given name album and lyric
        source.
        Also populates the lyric data from the file located at:
            static/lyrics/NAME.txt where NAME is the song name in lower case
            with punctuation removed.
        
        Parameters:
            name (string): the name of the song
            album (string): the name of the album that contains the song.
            lyric_source (string): the source where these lyrics were found.
        """
        self.name = name
        self.album = album
        self.lyrics = Lyrics(name)
        self.lyric_source = lyric_source

    def __repr__(self):
        return self.name

    def _check_current_word_match(lyrics1, lyrics2, cw_index1, cw_index2):
        """ A helper that checks the current words for a match """
        if lyrics1[cw_index1] == lyrics2[cw_index2]:
            Lyrics.mark_match(lyrics1[cw_index1], lyrics2[cw_index2])

    def _move_indices(lyrics1, lyrics2, cw_index1, cw_index2):
        """ A helper that moves the current index counters for the two songs.
        """
        # TODO: make sure not to run out the end of either song
        if len(lyrics1) - 1 == cw_index1:
            return cw_index1, cw_index2
        elif len(lyrics2) - 1 == cw_index2:
            return cw_index1 + 1, cw_index2
        elif lyrics1[cw_index1] < lyrics2[cw_index2]:
            return cw_index1 + 1, cw_index2
        else:
            return cw_index1, cw_index2 + 1

    def compare_to_song(self, other_song):
        """ Finds all the words in common between this song and the supplied
        song.

        Parameters:
            other_song (Song): the song to find matches from.
        """
        print(f"Comparing {self} and {other_song}")
        this_current_word_index = 0
        other_current_word_index = 0
        # Adding variable for ease
        this_lyrics = self.lyrics.sorted_lyrics
        other_lyrics = other_song.lyrics.sorted_lyrics

        while True:
            # If both songs are finished we can exit
            if ((len(this_lyrics) - 1 == this_current_word_index) and
                    (len(other_lyrics) - 1 and other_current_word_index)):
                print("Finishing the loop")
                break
            # Check the match
            Song._check_current_word_match(this_lyrics, other_lyrics,
                    this_current_word_index, other_current_word_index)
            # Move to the next index with the 'smaller' one
            this_current_word_index, other_current_word_index = Song._move_indices(
                    this_lyrics, other_lyrics,
                    this_current_word_index, other_current_word_index)

if __name__ == "__main__":
    card = Song("cardigan", "Folklore", "Musixmatch")
    bett = Song("betty", "Folklore", "Musixmatch")
    card.compare_to_song(bett)

    # Next step is to compare both of these and find all the matches. 
    # Once I have all the matches I can work on formatting the webpage for the
    # lyrics. 

    # After that I can work on uploading all the songs and finding the most
    # commonly used words
    # After that I can generalise the site to allow comparisons of multiple
    # songs, different ways of viewing matches and modifying searches etc.
