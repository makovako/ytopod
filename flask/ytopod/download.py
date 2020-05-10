import youtube_dl
from .models import Video
from . import socketio
import re

class MyLogger(object):
    """Logger class for youtube_dl Logger to tell yt-dl to print errors"""

    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    """Helper function for printing, when youtube-dl has finished downloading content."""

    if d['status'] == 'finished':
        filename = re.search(r'.*\/(.*)\..*',d["filename"]).group(1)
        socketio.emit("download",(f"Converting audio", 100, filename))
    if d['status'] == 'downloading':
        filename = re.search(r'.*\/(.*)\..*',d["filename"]).group(1)
        percent = d['_percent_str'].split('.')[0]
        socketio.emit("download",(f"Downloading {percent}%", percent, filename))
        # print(d['filename'], d['_percent_str'], d['_eta_str'])

def get_useful_information(info):
    """Extracts useful information from video."""

    result = {}
    result['description'] = info['description']
    result['id'] = info['id']
    result['thumbnail'] = info['thumbnail']
    result['title'] = info['title']
    result['uploader'] = info['uploader']
    return result

def download_video(video_url, root_path):
    ydl_opts = {
        "format": "bestaudio[ext=m4a]",
        "progress_hooks": [my_hook],
        "outtmpl": root_path + "/download/%(id)s.%(ext)s",
        "postprocessors": [{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'320'
        }]
    }
    
    with youtube_dl.YoutubeDL({"progress_hooks":[my_hook],"skip_download":"True"}) as ydl:
        try:
            info = get_useful_information(ydl.extract_info(video_url))
        except youtube_dl.utils.ExtractorError as error:
            return (False, f'Preblem with extracting: {str(error)}')
        except youtube_dl.utils.DownloadError as error:
            return (False, f'Problem with downloading: {str(error)}')


    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
        except youtube_dl.utils.DownloadError as error:
            return (False, f'Problem with downloading: {str(error)}')
    video = Video(info['id'], info['title'], info['description'], info['uploader'], info['thumbnail'])
    return (True, video)