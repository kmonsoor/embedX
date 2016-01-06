from .youtube import YouTube

supported = {
    YouTube: ['youtube', 'youtu.be'],
}


class OnlineVideo(object):
    url = None
    video_id = None
    instance = None

    # these templates must be defined by providing subclasses
    EMBED_SCRIPT = ''''''
    LINK_TEMPLATE = ''''''
    STATUS_LINK = ''''''

    def __init__(self, url=None):
        if url:
            # URL-specific dispatching to `provider` objects
            for provider_obj in supported:
                for x in supported[provider_obj]:
                    if x in url:
                        self.url = url
                        self.instance = provider_obj(self.url)
                        self.video_id = self.get_video_id()
            raise NotImplementedError

    def get_provider(self):
        return self.instance.__str__()

    def get_video_id(self):
        """Returns the unique ID extracted from the link of the video
        """
        self.video_id = self.instance.extract_id()
        return self.video_id

    def get_embed_code(self):
        if self.video_id is None:
            self.instance.extract_id()
        return self.EMBED_SCRIPT % ({'VIDEO_ID': self.video_id})

    def get_clean_link(self):
        if self.video_id is None:
            self.instance.extract_id()
        return self.LINK_TEMPLATE % ({'VIDEO_ID': self.video_id})

    def extract_id(self):
        """Extract the unique ID from the URL link, set it to `self.video_id`, and return the value.
        This method must be implemented by sub-class.
        :return: string ID of the video
        """
        raise NotImplementedError

    def check_if_alive(self):
        """Check if the video is available on the host server. Returns `True` if available, else `False`.
        This method is `lazy`-evaluated or only executes when called.
        :rtype: bool
        """
        from urllib2 import urlopen, URLError, HTTPError

        url = self.STATUS_LINK % ({'VIDEO_ID': self.video_id})
        try:
            response = urlopen(url)
        except (HTTPError, URLError):
            return False
        else:
            return True if response.code == 200 else False
