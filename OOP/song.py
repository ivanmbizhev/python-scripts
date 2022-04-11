class Song:
    """Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object repr the songs creator.
        duration (int): The duration of the song in seconds. Maybe zero
        """
    def __init__(self, title, artist, duration=0):
       
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist (Artist): The artist responsible ofr the album. 
        If not specified, the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist

        self.tracks = []
    
    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): A song to add.
            position (Optional): if specified, the song will be added to that position
                        in the track list - inserting it btw other songs of neccessary.
                        Otherwise, the song wil be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (list[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not a exclusive list of this arts's published albums.

    Methods:
        add_album: Use to add a new album ot the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (_type_): Album object to add to the list.
                if the album is already present, it will not be added again.
        """
        self.albums.append(album)