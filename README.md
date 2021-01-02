# Subplacer

Subplacer is a script that accepts a youtube link in the following format:
 https://www.youtube.com/watch?v=OXuxJaYsIvs
 and an Destination folder and does the following:
 1) Downloads the youtube video in .mp4 format
 2) Creates an .srt and .ass subtitle files from the Youtube 
 3) Creates a new video file with the subtitles 
 4) Deletes all downloaded and created files except the subtitled video.

 The new video will have the same name as the original video + "_with_subtitles" ending
<br>
<br>

## <b>Features that I will add soon</b>
* A loop in order to run the script multiple times with continue/quit option

## <b>Prerequisites</b>
* The chosen youtube link needs to has to have a transcription
* Python 3.8+
* [FFmpeg](https://ffmpeg.org/download.html)


## <b> Result example </b>
![](Images/sub.PNG)
