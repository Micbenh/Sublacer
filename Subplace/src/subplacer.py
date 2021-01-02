#from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime 
import time
import sys,os
sys.path.append(os.getcwd())
import utils.downloader as dwn
import subprocess
from pytube import YouTube 
import requests
import bs4

class Srt_maker:
    """
        A class that accepts a youtube video_id, saves it's transcript
        and creats a '.srt' file that contains the line number, start and end time stamps 
        and the collerated sentence to that timestamps  

        Attributes
        ----------
        video_id : str
            the unique id of a youtube video. 
            it can be usually found in the end of an url after the "v=..." 
            for example https://www.youtube.com/watch?v=xdq6Gz33khQ
    
    """
    def download_video(self):
        youtube_link = input("enter a youtube url to download: ")
        output_dir = input("Enter a directory location to save the youtube video: ")

        req = requests.get(youtube_link)
        html = bs4.BeautifulSoup(req.text)
        name = html.title.string.split("-")[0][:-1].replace(",","").replace("[",'').replace("]",'')
        dwn.download_video(youtube_link, output_dir, name)
        return youtube_link, output_dir, name

    #@trace
    def create_srt_file(self):
        """
        A function that creates an srt file from a video_id.
        :return: an ".srt" file 
        """
        # collect youtube link and download it to desired path
        link, output, name = self.download_video()
        name = name.replace(" [","")
        link = link.split("v=")
        cleaner = {
            ',': "",
            '"':"",
            "'":"",
            "@":"",
            "#":"",
            "$":"",
            "%":"",
            "^":"",
            "&":"",
            "*":"",
            "/":"",
            "\\":"",
            ".":"",
            ":":""
        }
        for k,v in cleaner.items():
            name = name.replace(k, v)

        #create captions 
        print(link[0] + 'v=' + link[-1])
        yt = YouTube(link[0] + 'v=' + link[-1])
        print(yt.captions.all())
        caption = yt.captions.get_by_language_code('a.en')
        print(caption.generate_srt_captions())

        srt = open(output + "\\" + "{}.srt".format(name), "w")
        srt.write(caption.generate_srt_captions())
        srt.close()
        print(name)
        time.sleep(2)
        
        #insert subtitles into video and delete unneeded files
        subprocess.call(['ffmpeg', '-i', r"{}\\{}.srt".format(output, name), '{}'.format(output) + "\\" + "{}.ass".format(name)])
        time.sleep(2)
        os.chdir(output)

        subprocess.call(['ffmpeg', '-i',"{}\\{}.mp4".format(output, name) ,'-vf' ,'ass={}'.format("{}.ass".format(name)) , '{}\\{}_with_subs.mp4'.format(output,name) ])
        time.sleep(3)
        os.remove(output + "\\" + name  + ".mp4")
        time.sleep(0.5)
        os.remove(output + "\\" + name + ".srt")
        time.sleep(0.5)
        os.remove(output + "\\" + name + ".ass")






video = Srt_maker()
video.create_srt_file()
