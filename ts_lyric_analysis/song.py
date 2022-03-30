# import functools

from flask import Blueprint, current_app, render_template
from ts_lyric_analysis.lyrics import Lyrics
from ts_lyric_analysis.db import get_db

bp = Blueprint("song", __name__, url_prefix="/song")
TEMPLATE_DIR = "songs/"
DB_SCRIPT_FN = "database/scripts/"

class Song:
    """ Contains all the information needed for the current song. Is also a
    blueprint for the flask application to view details about this song.

    Parameters:
        name (string): the name of the song
        album (string): the name of the album the song is on.
        track_number (int): the track number of the song on the album.
        lyrics (Lyrics): the lyrics of the song
        lyric_source (string): the source where there lyrics is from.
        is_from_the_vault (bool): whether or not the song is from the vault
            so that adjustments can be made to the title if required.

    Methods:
        __init__(name, album, lyric_source): creates a new Song object using
            the given name, album and lyric source. Assumes that the lyrics
            for the song are saved in an appropriately named file.
        compare_to_song(song): finds all the words in common between this
            song and the supplied one.
        display_lyrics(): readies the lyrics to be displayed on the webpage.
        make_song_from_db(db_value): turns the result returned from the
            database into a song object if it exists.
        make_songs_from_db(db_values): turns the results returned from the
            database into song objects.
    """
    def __init__(self,
                 name,
                 album,
                 track_number,
                 lyric_source,
                 is_from_the_vault=False):
        """ Creates an new song object with the given name album and lyric
        source.
        Also populates the lyric data from the file located at:
            static/lyrics/NAME.txt where NAME is the song name in lower case
            with punctuation removed.

        Parameters:
            name (string): the name of the song
            album (string): the name of the album that contains the song.
            track_number (int): the position of this song on the album.
            lyric_source (string): the source where these lyrics were found.
            is_from_the_vault (bool): whether the song is from the vault.
                False unless specified otherwise.
        """
        self.name = name
        self.album = album
        self.lyrics = Lyrics(name)
        self.track_number = track_number
        self.lyric_source = lyric_source
        self.is_from_the_vault = is_from_the_vault

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return (self.name == other.name
                and self.album == other.album
                and self.track_number == other.track_number
                and self.is_from_the_vault == other.is_from_the_vault)

    def _check_current_word_match(lyrics1, lyrics2, cw_index1, cw_index2):
        """ A helper that checks the current words for a match """
        if lyrics1[cw_index1] == lyrics2[cw_index2]:
            Lyrics.mark_match(lyrics1[cw_index1], lyrics2[cw_index2])

    def _move_indices(lyrics1, lyrics2, cw_index1, cw_index2):
        """ A helper that moves the current index counters for the two songs.
        """
        if len(lyrics1) - 1 == cw_index1:
            return cw_index1, cw_index2 + 1
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
        this_cw_idx = 0
        other_cw_idx = 0
        # Adding variable for ease
        this_lyrics = self.lyrics.sorted_lyrics
        other_lyrics = other_song.lyrics.sorted_lyrics

        while True:
            Song._check_current_word_match(this_lyrics,
                                           other_lyrics,
                                           this_cw_idx,
                                           other_cw_idx)
            # If we do not check the match before this exit condition the last
            # word is never checked
            if ((len(this_lyrics) - 1 == this_cw_idx) and
                    (len(other_lyrics) - 1 == other_cw_idx)):
                break

            this_cw_idx, other_cw_idx = Song._move_indices(
                    this_lyrics, other_lyrics,
                    this_cw_idx, other_cw_idx)

    def display_lyrics(self):
        """ Returns the original lyrics formatted to support display on the
        webpage.

        Returns:
            list<list<Word>: the words that make up this song. The first list
                contains each paragraph and the items in the second list is
                each line. It is important to return the word object not just a
                string so that further checking can be done in the html to add
                formatting
        """
        return self.lyrics.display_lyrics()

    def make_song_from_db(db_value):
        """ Turns the value from the database into a song object.

        Parameters:
            db_value (sqlite3.Row): the value to turn into a song.

        Returns:
            Song: the song created from the object. None if the db_value was
                None.
        """
        # The db_value includes the database ID which we do not need so ignore
        # it
        return Song(*db_value[1:])

    def make_songs_from_db(db_values):
        """ Turns the values from the database into a list of song objects. The
            returned list will be in the same order as the supplied values.

        Parameters:
            db_values (List<sqlite3.Row): the values to make into songs.

        Returns:
            list<Song>: the songs created from the supplied values.
        """
        return [Song.make_song_from_db(value) for value in db_values]


""" All the methods associated with the blueprint go beneath here.

Methods:
    show_lyrics(song_name): displays the lyrics of the given song.
    list_all_songs(): displays a list of all Taylor's songs.
"""

@bp.route("/<song_name>", methods=["GET"])
def show_lyrics(song_name):
    # TODO: generalise this once the database exists
    return render_template(f"{TEMPLATE_DIR}view_song_lyrics.html",
                           song=Song("betty", "Folklore", 2, "Musixmatch"))


@bp.route("")
def list_all_songs():
    # TODO: update this to do something more useful: maybe pretty album page.
    db = get_db()
    songs = []
    with current_app.open_resource(
            f"{DB_SCRIPT_FN}get_all_songs.sql") as f:
        result = db.execute(f.read().decode("utf8")).fetchall()
        songs = Song.make_songs_from_db(result)
    return render_template(f"{TEMPLATE_DIR}show_all_songs.html",
                           songs=songs)


if __name__ == "__main__":
    # card = Song("cardigan", "Folklore", "Musixmatch")
    bett = Song("betty", "Folklore", "Musixmatch")
    # card.compare_to_song(bett)

    # Next step is to compare both of these and find all the matches.
    # Once I have all the matches I can work on formatting the webpage for the
    # lyrics.

    # After that I can work on uploading all the songs and finding the most
    # commonly used words
    # After that I can generalise the site to allow comparisons of multiple
    # songs, different ways of viewing matches and modifying searches etc.
