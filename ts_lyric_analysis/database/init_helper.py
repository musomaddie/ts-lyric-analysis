from flask import current_app
from ts_lyric_analysis.database.store_song_info_in_db import list_debut_album_songs
from ts_lyric_analysis.database.store_song_info_in_db import list_fearless_album_songs

DB_SCRIPT_FN = "database/scripts/"

def _find_album_id(db, album_name):
    """ Helper to find the given album id from the database.

    Parameters:
        db: the database to search
        album_name: the album we are looking for

    Returns:
        int: the id of the album, -1 if the given album_name is not found.
    """
    with current_app.open_resource(f"{DB_SCRIPT_FN}select_album_id.sql") as f:
        result = db.execute(f.read().decode("utf8"),
                            ((album_name),)).fetchone()
        if result is None:
            return -1
        return result["id"]

def populate_albums(db):
    """ Populates the album information part of the database.  """
    # Debut album
    with current_app.open_resource(
            f"{DB_SCRIPT_FN}insert_album.sql") as f:
        db.execute(f.read().decode("utf8"),
                   ("Taylor Swift", 1),)
    # Fearless
    with current_app.open_resource(
            f"{DB_SCRIPT_FN}insert_album.sql") as f:
        db.execute(f.read().decode("utf8"),
                   ("Fearless (Taylor's Version)", 2))
    db.commit()

def populate_debut_album(db):
    """ Helper for init_db() that populates data from the début album. """
    da = list_debut_album_songs()
    a_id = _find_album_id(db, "Taylor Swift")

    for song in da:
        with current_app.open_resource(
                f"{DB_SCRIPT_FN}insert_song.sql") as f:
            db.execute(f.read().decode("utf8"),
                       (song[0], a_id, song[2], song[3], False),)
    db.commit()

def populate_fearless_album(db):
    """ Helper for init_db() that populates song data from the Fearless album.
    """
    f_songs = list_fearless_album_songs()
    a_id = _find_album_id(db, "Fearless (Taylor's Version)")

    for song in f_songs:
        val4 = False
        if len(song) == 5 and song[4]:
            val4 = True
        values = [song[0], a_id, song[2], song[3], val4]
        with current_app.open_resource(
                f"{DB_SCRIPT_FN}insert_song.sql") as f:
            db.execute(f.read().decode("utf8"), values)
        db.commit()
