def list_debut_album_songs():
    # I don't have to return the song object here as this is for db storage. I
    # just need the song title, album, track number and lyric source but I must
    # ensure the lyric file is created to avoid later issues.
    album = "Taylor Swift"
    return [("Tim McGraw", album, 1, "LyricFind"),
            ("Picture To Burn", album, 2, "LyricFind"),
            ("Teardrops On My Guitar", album, 3, "LyricFind"),
            ("A Place In This World", album, 4, "LyricFind"),
            ("Cold As You", album, 5, "LyricFind"),
            ("The Outside", album, 6, "MusixMatch"),
            ("Tied Together With A Smile", album, 7, "LyricFind"),
            ("Stay Beautiful", album, 8, "LyricFind"),
            ("Should've Said No", album, 9, "LyricFind"),
            ("Mary's Song (Oh My My My)", album, 10, "MusixMatch"),
            ("Our Song", album, 11, "MusixMatch"),
            ("I'm Only Me When I'm With You", album, 12, "LyricFind"),
            ("Invisible", album, 13, "LyricFind")]

def list_fearless_album_songs():
    album = "Fearless"
    return [("Fearless", album, 1, "Musixmatch"),
            ("Fifteen", album, 2, "Musixmatch"),
            ("Love Story", album, 3, "LyricFind"),
            ("Hey Stephen", album, 4, "Musixmatch"),
            ("White Horse", album, 5, "LyricFind"),
            ("You Belong With Me", album, 6, "Musixmatch"),
            ("Breathe", album, 7, "Musixmatch"),
            ("Tell Me Why", album, 8, "LyricFind"),
            ("You're Not Sorry", album, 9, "Musixmatch"),
            ("The Way I Loved You", album, 10, "Musixmatch"),
            ("Forever & Always", album, 11, "LyricFind"),
            ("The Best Day", album, 12, "LyricFind"),
            ("Change", album, 13, "Musixmatch"),
            ("Jump Then Fall", album, 14, "LyricFind"),
            ("Untouchable", album, 15, "LyricFind"),
            ("Forever & Always (piano version)", album, 16, "Musixmatch"),
            ("Come In With The Rain", album, 17, "LyricFind"),
            ("Superstar", album, 18, "Musixmatch"),
            ("The Other Side Of The Door", album, 19, "LyricFind"),
            ("Today Was A Fairytale", album, 20, "LyricFind"),
            ("You All Over Me", album, 21, "LyricFind", True),
            ("Mr. Perfectly Fine", album, 22, "LyricFind", True),
            ("We Were Happy", album, 23, "LyricFind", True),
            ("That's When", album, 24, "LyricFind", True),
            ("Don't You", album, 25, "LyricFind", True),
            ("Bye Bye Baby", album, 26, "Musixmatch", True)]

def list_speak_now_album_songs():
    album = "Speak Now"
    return [("Mine", album, 1, "LyricFind"),
            ("Sparks Fly", album, 2, "LyricFind"),
            ("Back To December", album, 3, "LyricFind"),
            ("Speak Now", album, 4, "Musixmatch"),
            ("Dear John", album, 5, "Musixmatch"),
            ("Mean", album, 6, "Musixmatch"),
            ("The Story Of Us", album, 7, "Musixmatch"),
            ("Never Grow Up", album, 8, "Musixmatch"),
            ("Enchanted", album, 9, "LyricFind"),
            ("Better Than Revenge", album, 10, "LyricFind"),
            ("Innocent", album, 11, "Musixmatch"),
            ("Haunted", album, 15, "LyricFind"),
            ("Last Kiss", album, 16, "LyricFind"),
            ("Long Live", album, 17, "Genius Lyrics"),
            ("Ours", album, 18, "Musixmatch"),
            ("If This Was A Movie", album, 19, "LyricFind"),
            ("Superman", album, 20, "LyricFind")]

def list_red_album_songs():
    album = "Red"
    return [
        ("State of Grace", album, 1, "Musixmatch"),
        ("Red", album, 2, "Musixmatch"),
        ("Treacherous", album, 3, "LyricFind"),
        ("I Knew You Were Trouble", album, 4, "Genius Lyrics"),
        ("All Too Well", album, 5, "LyricFind"),
        ("22", album, 6, "LyricFind"),
        ("I Almost Do", album, 7, "Musixmatch"),
        ("We Are Never Ever Getting Back Together", album, 8, "LyricFind"),
        ("Stay Stay Stay", album,  9, "Musixmatch"),
        ("The Last Time", album, 10, "LyricFind"),
        ("Holy Ground", album, 11, "AZ Lyrics"),
        ("Sad Beautiful Tragic", album, 12, "Musixmatch"),
        ("The Lucky One", album, 13, "Genius Lyrics"),
        ("Everything Has Changed", album, 14, "LyricFind"),
        ("Starlight", album, 15, "Musixmatch"),
        ("Begin Again", album, 16, "Musixmatch"),
        ("The Moment I Knew", album, 17, "Musixmatch"),
        ("Come Back... Be Here", album, 18, "Musixmatch"),
        ("Girl At Home", album, 19, "Musixmatch"),
        ("State of Grace (Acoustic Version)", album, 20, "Musixmatch"),
        ("Ronan", album, 21, "LyricFind"),
        ("Better Man", album, 22, "Musixmatch", True),
        ("Nothing New", album, 23, "Musixmatch", True),
        ("Babe", album, 24, "Musixmatch", True),
        ("Message in a Bottle", album, 25, "LyricFind", True),
        ("I Bet You Think About Me", album, 26, "Musixmatch", True),
        ("Forever Winter", album, 27, "Musixmatch", True),
        ("Run", album, 28, "Musixmatch", True),
        ("The Very First Night", album, 29, "LyricFind", True),
        ("All Too Well (10 minute version)", album, 30, "LyricFind", True)
    ]
