from feedgen.feed import FeedGenerator
from flask import request, current_app as app
import os

def generate_feed(videos):
    """Creates feed from items from db"""

    baseurl = request.host_url

    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.title('My feed')
    fg.link(href=baseurl, rel='alternate')
    fg.description('Some description')
    fg.author({"name":"makovako", "email":"test@example.com"})
    fg.podcast.itunes_owner(name='makovako',email='test@example.com')
    
    fg.podcast.itunes_author("makovako")

    # videos = get_all_videos()
    for video in videos:
        fe = fg.add_entry()
        fe.id('download/' + video.youtube_id)
        fe.title(video.title)
        fe.description(video.description)
        fe.podcast.itunes_author(video.uploader)
        fe.podcast.itunes_image(video.thumbnail)
        fe.enclosure(baseurl+'download/'+video.youtube_id+'.mp3',0,'audio/mpeg')
    fg.rss_str(pretty=True)
    fg.rss_file(os.path.join(app.root_path, 'download', 'feed.xml'))