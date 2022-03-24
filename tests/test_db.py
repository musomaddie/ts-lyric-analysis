from ts_lyric_analysis.db import get_db, init_db
from ts_lyric_analysis.database.store_song_info_in_db import list_debut_album_songs

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

        a_id = album["id"]

        # Get the songs
        songs_from_db = [s["song_title"] for s in db.execute(
            """ SELECT song_title
                FROM song_info
                WHERE album_id = ?; """, (a_id,)).fetchall()]
        for song in _get_songs_from_album("Taylor Swift"):
            assert song[0] in songs_from_db
