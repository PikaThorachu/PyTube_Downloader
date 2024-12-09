# import packages
from pytube import YouTube
import os
import eyed3

# List class Song objects for download
src_files: list = []

# Define destination path for downloads as constant
# Make sure you don't use relative path
DEST: str = "YOUR DESTINATION FOLDER PATH GOES HERE"

# Define the class "Song" to store metadata for each song
class Song():
    def __init__(self, url, title=None, artist=None, album=None, album_artist=None, track_number=None, file_path=None):
        self.url = url
        self.title = title
        self.artist = artist
        self.album = album
        self.album_artist = album_artist
        self.track_number = track_number
        self.file_path = file_path

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
            src.file_path = new_file

        except:
            # Exception handling
            print(f"{src.url} failed to download")

        # WAIT FOR THE FILE TO COMPLETE DOWNLOADING
        # CHECK FOR THE FILE BEFORE RUNNING HELPER FUNCTION
        # Need to code this section still

        # Once the file has downloaded, then execute helper function
        Song.metadata_updater(src)


    def metadata_updater(src):
        # load file
        audiofile = eyed3.load(src.file_path)

        # Update tags
        audiofile.tag.artist = src.artist

        # Save file
        audiofile.tag.save()
    
def main():
    # Input a list of Song objects to process
    src_files: list = []
    for src in src_files:
        Song.download_yt(src, DEST)
    
    print("Your file download has completed")

main()