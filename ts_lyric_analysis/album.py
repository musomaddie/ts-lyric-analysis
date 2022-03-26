class Album:
    """ Contains information for an album.

    Parameters:
        name (string): the name of the album. Name should not include
            ('Taylor's Version') even if it is true for ease.
        songs (list<Song>): all the songs on the album (ordered by track
            number).
        order_of_release (int): where this album falls in the release
            order. i.e. Début is 1, fearless 2, etc. For singles this will
            be 0.
        release_year (int): the year this album was released. In the case of
            Taylor's versions this remains the year of the original album
            release.
        is_taylors_version: (bool): true if this album is a Taylor's
            Version.

    Methods:
        __init__(name, order_of_release, release_year, is_taylors_version):
            creates a new Album object using the given name and boolean.
        get_album_name(): returns the album name formatted fully.
    """
    def __init__(self,
                 name,
                 order_of_release,
                 release_year,
                 is_taylors_version):
        """ Creates a new album object with the provided values.
        Does not populate the song list, this needs to be done explicitly
        afterwards as this assumes the songs require the album information.

        Parameters:
            name (string): the name of the album
            order_of_release (int): where the album falls in terms of release
                order.
            release_year (int): the year the album was released.
            is_taylors_version (bool): true if this album is a taylors version.
        """
        self.name = name
        # Initially empty as the album needs to be created before the songs.
        self.songs = []
        self.order_of_release = order_of_release
        self.release_year = release_year
        self.is_taylors_version = is_taylors_version

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def get_album_name(self):
        """ Returns the formatted name of the album. If the album is taylors
        version '(Taylor's Version)' is added to the end of the album title.

        Returns:
            string: formatted album name.
        """
        if self.is_taylors_version:
            return f"{self.name} (Taylor's Version)"
        return self.name
