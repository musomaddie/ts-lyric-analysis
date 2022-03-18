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


if __name__ == "__main__":
    card = Song("cardigan", "Folklore", "Musixmatch")
    bett = Song("betty", "Folklore", "Musixmatch")

    # Next step is to compare both of these and find all the matches. 
    # Once I have all the matches I can work on formatting the webpage for the
    # lyrics. 

    # After that I can work on uploading all the songs and finding the most
    # commonly used words
    # After that I can generalise the site to allow comparisons of multiple
    # songs, different ways of viewing matches and modifying searches etc.
