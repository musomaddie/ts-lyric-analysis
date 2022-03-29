from flask import current_app
from ts_lyric_analysis.database.store_song_info_in_db import list_debut_album_songs
from ts_lyric_analysis.database.store_song_info_in_db import list_fearless_album_songs
from ts_lyric_analysis.database.store_song_info_in_db import list_speak_now_album_songs

DB_SCRIPT_FN = "database/scripts/"

def _get_songs_from_album(album_name):
    """ Helper that gets the song list for the given album.

    Parameters:
        album_name: the name of the album.

    Returns:
        list<?>: the information for all songs in the album.
    """
    if album_name == "Taylor Swift":
        return list_debut_album_songs()
    elif album_name == "Fearless":
        return list_fearless_album_songs()
    elif album_name == "Speak Now":
        return list_speak_now_album_songs()
    return []

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
                   ("Taylor Swift", 1, 2006, False))
    # Fearless
    with current_app.open_resource(
            f"{DB_SCRIPT_FN}insert_album.sql") as f:
        db.execute(f.read().decode("utf8"),
                   ("Fearless", 2, 2008, True))

    # Speak Now
    with current_app.open_resource(
            f"{DB_SCRIPT_FN}insert_album.sql") as f:
        db.execute(f.read().decode("utf8"),
                   ("Speak Now", 3, 2010, False))
    db.commit()

def populate_songs(db, album_name):
    """ Helper for init_db() that populates all the songs of the given album
    name.
    """
    album_song_list = _get_songs_from_album(album_name)
    a_id = _find_album_id(db, album_name)
    if a_id == -1:
        print(f"Couldn't find {album_name} in the database.")

    for song in album_song_list:
        val4 = False
        if len(song) == 5 and song[4]:
            val4 = True
        values = [song[0], a_id, song[2], song[3], val4]
        with current_app.open_resource(
                f"{DB_SCRIPT_FN}insert_song.sql") as f:
            db.execute(f.read().decode("utf8"), values)
        db.commit()
