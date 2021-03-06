import pytest

from ts_lyric_analysis.album import Album
from ts_lyric_analysis.database.songs_for_db import debut_songs
from ts_lyric_analysis.database.songs_for_db import evermore_songs
from ts_lyric_analysis.database.songs_for_db import fearless_songs
from ts_lyric_analysis.database.songs_for_db import folklore_songs
from ts_lyric_analysis.database.songs_for_db import lover_songs
from ts_lyric_analysis.database.songs_for_db import n1989_songs
from ts_lyric_analysis.database.songs_for_db import red_songs
from ts_lyric_analysis.database.songs_for_db import reputation_songs
from ts_lyric_analysis.database.songs_for_db import singles_songs
from ts_lyric_analysis.database.songs_for_db import speak_now_songs
from ts_lyric_analysis.db import get_db, init_db
from ts_lyric_analysis.song import Song

ALL_ALBUM_NAMES = ["Taylor Swift",
                   "Fearless",
                   "Speak Now",
                   "Red",
                   "1989",
                   "reputation",
                   "Lover",
                   "folklore",
                   "evermore",
                   "Singles"]

def _get_songs_from_album(album_name):
    if album_name == "Taylor Swift":
        return debut_songs()
    if album_name == "Fearless":
        return fearless_songs()
    if album_name == "Speak Now":
        return speak_now_songs()
    if album_name == "Red":
        return red_songs()
    if album_name == "1989":
        return n1989_songs()
    if album_name == "reputation":
        return reputation_songs()
    if album_name == "Lover":
        return lover_songs()
    if album_name == "folklore":
        return folklore_songs()
    if album_name == "evermore":
        return evermore_songs()
    if album_name == "Singles":
        return singles_songs()
    return []

def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr("ts_lyric_analysis.db.init_db", fake_init_db)
    result = runner.invoke(args=["init-db"])
    assert "Initialized" in result.output
    assert Recorder.called


@pytest.mark.parametrize("album_name", ALL_ALBUM_NAMES)
def test_init_album_success(app, album_name):
    with app.app_context():
        init_db()
        db = get_db()
        album_db = db.execute(
            """ SELECT * FROM album_info WHERE album_name = ? """,
            (album_name,)).fetchone()
        assert album_db is not None

        # This check may seem somewhat pointless but it's important to check
        # that an album object can be created successfully from the information
        # from the db.
        album_obj = Album(*album_db[1:])
        assert album_name == album_obj.name

@pytest.mark.parametrize("album_name", ALL_ALBUM_NAMES)
def test_init_songs_success(app, album_name):
    """ Testing this makes the tests take longer, but I believe it is important
    to test this to avoid future issues, and to make the process of writing the
    adding script a bit easier.
    """
    with app.app_context():
        init_db()
        db = get_db()

        song_list = _get_songs_from_album(album_name)
        assert len(song_list) > 0, f"No songs were found from {album_name}."

        for song in song_list:
            song_db = db.execute(
                """ SELECT * FROM song_info WHERE song_title = ? """,
                (song[0],)).fetchone()
            assert song_db is not None

            # This may seem a bit pointless, but it's important to check that
            # the song object can be successfully created. It would be extreme
            # to check every value as it will be correct as long as the
            # provided data is.
            song_obj_db = Song(song_db["song_title"],
                               album_name,
                               song_db["track_number"],
                               song_db["lyric_source"],
                               song_db["is_from_the_vault"])
            assert song_obj_db.name == song[0]
