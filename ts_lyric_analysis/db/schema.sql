-- INITIALISE the database 
-- Drop any existing tables

DROP TABLE IF EXISTS song_info;
DROP TABLE IF EXISTS album_info;

CREATE TABLE album_info(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	album_name TEXT NOT NULL,
	position INTEGER
);

CREATE TABLE song_info(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	song_title TEXT NOT NULL,
	album_id INTEGER NOT NULL,
	track_number INTEGER NOT NULL,
	lyric_source TEXT NOT NULL,
	is_from_the_vault BOOLEAN NOT NULL,
	FOREIGN KEY (album_id) REFERENCES album_info (id)
);
