from flask import current_app

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
            f"{DB_SCRIPT_FN}insert_debut_album.sql") as f:
        db.executescript(f.read().decode("utf8"))
    db.commit()

def populate_debut_album(db):
    """ Helper for init_db() that populates data from the début album. """
    # Including import here to avoid circular dependencies
    from ts_lyric_analysis.database.store_song_info_in_db import list_debut_album_songs
    da = list_debut_album_songs()
    a_id = _find_album_id(db, "Taylor Swift")

    for song in da:
        with current_app.open_resource(
                f"{DB_SCRIPT_FN}insert_song.sql") as f:
            db.execute(f.read().decode("utf8"),
                       (song[0], a_id, song[2], song[3], False),)
    db.commit()
