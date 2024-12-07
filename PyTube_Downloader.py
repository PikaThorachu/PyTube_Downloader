# import packages
from pytube import YouTube
from moviepy import *
import os

# List YouTube URLs for download
src_files: list = []

# Define destination path for downloads as constant
DEST: str = "YOUR DESTINATION PATH GOES HERE"

# function to download the youtube file
def download_yt(src: str, dest: str):
    # Create object using YouTube package
    try:
        yt = YouTube(src)
        output = yt.streams.get_audio_only().download(output_path=dest)
        # split file into base and extension 
        # since ext not needed use _
        base, _ = os.path.splitext(output)
        # convert file to MP3
        new_file = base + '.mp3'
        # rename mp3 file
        os.rename(output, new_file)
    except:
        # Exception handling
        print(f"{src} failed to download")
    
def main():
    for src in src_files:
        download_yt(src, DEST)

main()