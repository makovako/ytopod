def extract_video_id(url):
    url_split = url.split('?')
    if len(url_split) < 2:
        return null
    for param in url_split[1].split('&'):
        key, value = param.split("=")
        if key == "v":
            return value
    return null