import yt_dlp

PLATLIST_URL = 'https://youtube.com/playlist?list=PL-bHfboOTFi4ljYahMOoxlT-uRlOyvItC&si=8lDiSzJBN6mm6xcA'
DIR = 'C:\\Youtube'

ydl_opts = {
        'format': 'worst',
        'outtmpl':f'{DIR}/%(playlist_title)s/%(title)s.%(ext)s',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([PLATLIST_URL])
    print(f"playlist download successfully to {DIR}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")