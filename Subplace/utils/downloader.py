from pytube import YouTube as yt
import os

def download_video(link, output_path,file_name):
    """
    A function that downloads a youtube video
    """
    vid = yt(link)
    stream = vid.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(output_path, filename=file_name)
