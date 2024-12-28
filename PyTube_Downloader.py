# import packages
from pytube import YouTube, extract

# List class Song objects for download
src_files: list = []

# Define destination path for downloads as constant
# Make sure you don't use relative path
DEST: str = "/home/pikathor/workspace/github.com/PikaThorachu/Real_Python/PyTube/Downloaded"

# Define the class "Song" to store metadata for each song
class Song():
    def __init__(self, url: str, title: str=None, artist: str=None, album: str=None, album_artist: str=None, track_number: int=None, track_duration: int=None, file_path: str=None):
        self.url = url
        self.title = title
        self.artist = artist
        self.album = album
        self.album_artist = album_artist
        self.track_number = track_number
        self.track_duration = track_duration
        self.file_path = file_path

    # function to download the youtube file
    # Moved this function to be a method of class Song
    def download_yt(src, dest: str) -> None:
        
        # Create object using YouTube package
        try:
            yt = YouTube(src.url)
                # Once figure out the next step (convert to MP3, set on_complete_callback to file conversion functoin)
            yt.streams.get_audio_only().download(output_path=dest)
            

        except:
            # Exception handling
            print(f"{src.url} failed to download")

    def extract_youtube_metadata(src) -> dict:
        youtube_metadata_dict = extract.metadata(src.url)
        print(youtube_metadata_dict.values())
    
def main():
    # Input a list of Song objects to process
    src_files: list = [
        Song("https://youtu.be/bcAEiSP-KUA")
        ]
    for src in src_files:
        Song.download_yt(src, DEST)
    
    print("Your file download has completed")

main()