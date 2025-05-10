# def make_album(album_name, artist_name, song_count=None):
#     """Album dictionaries"""
#     album = {'Album': album_name.title(), 'Artist': artist_name.title()}
#     if song_count:
#         album['Songs'] = song_count
#     return album

# music = make_album('stand up and scream', 'asking alexandria', song_count=13)
# print(music)

# music = make_album('dark side of the moon', 'Pink Floyd')
# print(music)

# music = make_album('deadbeat', 'jack kays')
# print(music)

def make_album(album_name, artist_name, song_count=None):
    """Album dictionaries"""
    album = {'Album': album_name.title(), 'Artist': artist_name.title()}
    if song_count:
        album['Songs'] = song_count
    return album

album = make_album('Stand up and Scream', 'Asking Alexandria', song_count=13)
print(album)
