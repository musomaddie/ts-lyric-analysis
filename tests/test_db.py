from ts_lyric_analysis.database.store_song_info_in_db import list_debut_album_songs
from ts_lyric_analysis.db import get_db, init_db
from ts_lyric_analysis.song import Song

def _get_songs_from_album(album_name):
    if album_name == "Taylor Swift":
        return list_debut_album_songs()
    return []

def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr("ts_lyric_analysis.db.init_db", fake_init_db)
    result = runner.invoke(args=["init-db"])
    assert "Initialized" in result.output
    assert Recorder.called

def test_init_debut_album(app):
    with app.app_context():
        init_db()
        db = get_db()
        # Assert the album was added correctly
        album = db.execute(
            """SELECT *
            FROM album_info
            WHERE album_name = 'Taylor Swift'""").fetchone()
        assert album is not None
        assert album["order_of_release"] == 1

def test_init_debut_album_songs(app):
    """ Testing this makes the tests take longer, but I believe it is important
    to test this to avoid future issues, and to make the process of writing the
    adding script a bit easier.
    """
    with app.app_context():
        init_db()
        db = get_db()

        for song in _get_songs_from_album("Taylor Swift"):
            song_db = db.execute(
                """ SELECT *
                    FROM song_info
                    WHERE song_title = ? """, (song[0],)).fetchone()
            assert song_db is not None
            song_obj = Song(song_db["song_title"],
                            "Taylor Swift",
                            song_db["track_number"],
                            song_db["lyric_source"],
                            song_db["is_from_the_vault"])
            assert song_obj == Song(song[0],
                                    song[1],
                                    song[2],
                                    song[3],
                                    False)

def test_init_fearless_album(app):
    with app.app_context():
        init_db()
        db = get_db()
        album = db.execute(
            """ SELECT *
                FROM album_info
                WHERE album_name = "Fearless (Taylor's Version)" """
        ).fetchone()

        assert album is not None
        assert album["album_name"] == "Fearless (Taylor's Version)"

def test_init_fearless_album_songs(app):
    album_name = "Fearless (Taylor's Version)"
    with app.app_context():
        init_db()
        db = get_db()

        for song in _get_songs_from_album(album_name):
            song_db = db.execute(
                """ SELECT *
                    FROM song_info
                    WHERE song_title = ? """,
                (song[0],)).fetchone()
            assert song_db is not None

            song_obj_db = Song(song_db["song_title"],
                               album_name,
                               song_db["track_number"],
                               song_db["lyric_source"],
                               song_db["is_from_the_vault"])
            if len(song) == 4:
                song = list(song) + [False]
            song_obj_test = Song(**song)
            assert song_obj_db == song_obj_test
