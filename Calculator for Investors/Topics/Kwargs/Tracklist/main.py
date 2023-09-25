def tracklist(**kwargs):
    for key, value in kwargs.items():
        print(key)
        for album, song in value.items():
            print(f'ALBUM: {album} TRACK: {song}')
