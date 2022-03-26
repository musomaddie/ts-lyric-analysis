import pytest

from ts_lyric_analysis.album import Album

@pytest.fixture
def album():
    """ Creates an album object for testing. """
    return Album("Testing", 1, 2000, False)

@pytest.fixture
def album_ts_version():
    """ Creates an album that is taylors version. """
    return Album("Testing", 1, 2000, True)

def test_setup(album):
    assert album.name == "Testing"
    assert album.order_of_release == 1
    assert album.release_year == 2000
    assert not album.is_taylors_version

def test_eq_identical(album):
    comp_album = Album("Testing", 1, 2000, False)
    assert album == comp_album

def test_eq_different(album):
    comp_album = Album("Not Testing", 2, 2000, False)
    assert not album == comp_album

def test_eq_matches_diff_details(album):
    comp_album = Album("Testing", 2, 2002, True)
    assert album == comp_album

def test_repr(album):
    assert album.__repr__() == "Testing"

def test_get_album_name(album):
    assert album.get_album_name() == "Testing"

def test_get_album_name_ts_version(album_ts_version):
    assert album_ts_version.get_album_name() == "Testing (Taylor's Version)"
