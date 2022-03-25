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
            ("Invisible", album, 13, "LyricFind")
    ]

def list_fearless_album_songs():
    album = "Fearless (Taylor's Version)"
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
