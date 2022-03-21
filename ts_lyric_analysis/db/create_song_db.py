from ts_lyric_analysis.song import Song

def debut_album():
    # I don't have to return the song object here as this is for db storage. I
    # just need the song title, album, track number and lyric source but I must
    # ensure the lyric file is created to avoid later issues.
    album = "Taylor Swift"
    return [("Time McGraw", album, 1, "LyricFind"),
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

def populate_db():
    # Making all the songs song objects takes a while. Hopefully when this is
    # deployed I can just do this once at the start and then refer to the
    # existing objects. Creating new 'Song' objects is costly in terms of time.
    da = debut_album()

if __name__ == "__main__":
    populate_db()
