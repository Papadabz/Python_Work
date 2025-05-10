def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title, 'songs': songs}
    return album

while True:
    print("\nEnter album information.")
    print("(Enter 'q' to quit at any time)")

    artist = input("\nArtist Name: ")
    if artist == 'q':
        break
       
    title = input("Album Name: ")
    if title == 'q':
        break

    songs = input('Song Count: ')
    if songs == 'q':
        break

    album = make_album(artist, title, songs)
    print(album)

            
