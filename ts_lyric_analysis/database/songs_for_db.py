def debut_songs():
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

def fearless_songs():
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

def speak_now_songs():
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

def red_songs():
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

def n1989_songs():
    album = "1989"
    return [
        ("Welcome To New York", album, 1, "Musixmatch"),
        ("Blank Space", album, 2, "LyricFind"),
        ("Style", album, 3, "Musixmatch"),
        ("Out Of The Woods", album, 4, "Musixmatch"),
        ("All You Had To Do Was Stay", album, 5, "Musixmatch"),
        ("Shake It Off", album, 6, "Musixmatch"),
        ("I Wish You Would", album, 7, "LyricFind"),
        ("Bad Blood", album, 8, "LyricFind"),
        ("Wildest Dreams", album, 9, "Musixmatch", True),
        ("How You Get the Girl", album, 10, "LyricFind"),
        ("This Love", album, 11, "Musixmatch"),
        ("I Know Places", album, 12, "LyricFind"),
        ("Clean", album, 13, "LyricFind"),
        ("Wonderland", album, 14, "LyricFind"),
        ("You Are In Love", album, 15, "LyricFind"),
        ("New Romantics", album, 16, "Musixmatch")
    ]

def reputation_songs():
    album = "reputation"
    return [
        ("...Ready for It?", album, 1, "LyricFind"),
        ("End Game", album, 2, "Musixmatch"),
        ("I Did Something Bad", album, 3, "LyricFind"),
        ("Don't Blame Me", album, 4, "Musixmatch"),
        ("Delicate", album, 5, "Musixmatch"),
        ("Look What You Made Me Do", album, 6, "Musixmatch"),
        ("So It Goes...", album, 7, "Musixmatch"),
        ("Gorgeous", album, 8, "Musixmatch"),
        ("Getaway Car", album, 9, "LyricFind"),
        ("King of My Heart", album, 10, "LyricFind"),
        ("Dancing With Our Hands Tied", album, 11, "LyricFind"),
        ("Dress", album, 12, "LyricFind"),
        ("This Is Why We Can't Have Nice Things", album, 13, "LyricFind"),
        ("Call It What You Want", album, 14, "Musixmatch"),
        ("New Year's Day", album, 15, "LyricFind")
    ]

def lover_songs():
    album = "Lover"
    return [
        ("I Forgot That You Existed", album, 1, "LyricFind"),
        ("Cruel Summer", album, 2, "Musixmatch"),
        ("Lover", album, 3, "LyricFind"),
        ("The Man", album, 4, "Musixmatch"),
        ("The Archer", album, 5, "Musixmatch"),
        ("I Think He Knows",  album, 6, "LyricFind"),
        ("Miss Americana & The Heartbreak Prince", album, 7, "Musixmatch"),
        ("Paper Rings", album, 8, "LyricFind"),
        ("Cornelia Street", album, 9, "LyricFind"),
        ("Death By A Thousand Cuts", album, 10, "LyricFind"),
        ("London Boy", album, 11, "Musixmatch"),
        ("Soon You'll Get Better", album, 12, "Musixmatch"),
        ("False God", album, 13, "Musixmatch"),
        ("You Need to Calm Down", album, 14, "Musixmatch"),
        ("Afterglow", album, 15, "LyricFind"),
        ("ME!", album, 16, "LyricFind"),
        ("It's Nice To Have A Friend", album, 17, "AZ Lyrics"),
        ("Daylight", album, 18, "LyricFind")
    ]

def folklore_songs():
    album = "folklore"
    return [
        ("the 1", album, 1, "Musixmatch"),
        ("cardigan", album, 2, "LyricFind"),
        ("the last great american dynasty", album, 3, "Musixmatch"),
        ("exile", album, 4, "LyricFind"),
        ("my tears ricochet", album, 5, "Musixmatch"),
        ("mirrorball", album, 6, "LyricFind"),
        ("seven", album, 7, "LyricFind"),
        ("august", album, 8, "LyricFind"),
        ("this is me trying", album, 9, "LyricFind"),
        ("illicit affairs", album, 10, "Musixmatch"),
        ("invisible string", album, 11, "LyricFind"),
        ("mad woman", album, 12, "LyricFind"),
        ("epiphany", album, 13, "Musixmatch"),
        ("betty", album, 14, "LyricFind"),
        ("peace", album, 15, "Musixmatch"),
        ("hoax", album, 16, "LyricFind"),
        ("the lakes", album, 17, "Musixmatch")
    ]

def evermore_songs():
    album = "evermore"
    return [
        ("willow", album, 1, "Musixmatch"),
        ("champagne problems", album, 2, "Musixmatch"),
        ("gold rush", album, 3, "Musixmatch"),
        ("'tis the damn season", album, 4, "Musixmatch"),
        ("tolerate it", album, 5, "LyricFind"),
        ("no body, no crime", album, 6, "LyricFind"),
        ("happiness", album, 7, "AZ Lyrics"),
        ("dorothea", album, 8, "LyricFind"),
        ("coney island", album, 9, "LyricFind"),
        ("ivy", album, 10, "Musixmatch"),
        ("cowboy like me", album, 11, "LyricFind"),
        ("long story short", album, 12, "LyricFind"),
        ("marjorie", album, 13, "LyricFind"),
        ("closure", album, 14, "Genius Lyrics"),
        ("evermore", album, 15, "LyricFind"),
        ("right where you left me", album, 16, "Musixmatch"),
        ("it's time to go", album, 17, "Musixmatch")
    ]

def singles_songs():
    album = "Singles"
    return [
        ("Only The Young", album, 0, "LyricFind"),
        ("Beautiful Ghosts", album, 0, "Musixmatch"),
        ("Christmas Tree Farm", album, 0, "LyricFind"),
        ("Safe & Sound", album, 0, "LyricFind"),
        ("Eyes Open", album, 0, "Musixmatch"),
        ("Sweeter Than Fiction", album, 0, "LyricFind"),
        ("Crazier", album, 0, "Musixmatch")
    ]
