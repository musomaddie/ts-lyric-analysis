from ts_lyric_analysis.db import get_db

def test_get_open_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()
