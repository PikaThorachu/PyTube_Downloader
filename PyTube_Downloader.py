# import packages
from pytube import YouTube
import eyed3
import os

# List class Song objects for download
src_files: list = []

# Define destination path for downloads as constant
# Make sure you don't use relative path
DEST: str = "YOUR DEST GOES HERE"

# Define the class "Song" to store metadata for each song
class Song():
    def __init__(self, url, title=None, artist=None, album=None, album_artist=None, track_number=None, file_name=None):
        self.url = url
        self.title = title
        self.artist = artist
        self.album = album
        self.album_artist = album_artist
        self.track_number = track_number
        self.file_name = file_name

    # function to download the youtube file
    # Moved this function to be a method of class Song
    def download_yt(src, dest: str):
        
        # Create object using YouTube package
        try:
            yt = YouTube(src.url)
            output = yt.streams.get_audio_only().download(output_path=dest)
            # split file into base and extension 
            # since ext not needed use _
            base, _ = os.path.splitext(output)
            # convert file to MP3
            new_file = base + '.mp3'
            # rename mp3 file
            os.rename(output, new_file)
            src.file_name = new_file

        except:
            # Exception handling
            print(f"{src.url} failed to download")
    
def main():
    # Input a list of Song objects to process
    src_files: list = []
    for src in src_files:
        Song.download_yt(src, DEST)
    
    print("Your file download has completed")

main()