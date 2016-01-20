from urlparse import urlparse, parse_qs

"""
Generate responsive, embeddable HTML/JS code from URL of online content
"""


class OnlineContent(object):
    """
    Object to represent a single content on Internet which can be accessed through a link.
    After initiating the `OnlineContent` object using its URL, embeddable code can be generated.
    Embeddable code generation is offline, by default.
    However, by using oEmbed protocol, it can be generated from the host site using its own API.

    >>> from embedx import OnlineContent
    >>> content = OnlineContent('http://www.youtube.com/watch?v=_lOT2p_FCvA')
    >>> content.extract_id()
    '_lOT2p_FCvA'
    >>> content.get_embed_code()
    "<div class='embed-container'><iframe src='http://www.youtube.com/embed/_lOT2p_FCvA' 'frameborder='0'allowfullscreen></iframe></div>"

    >>> content = OnlineContent('https://twitter.com/codinghorror/status/686254714938200064')
    >>> content.extract_id()
    '686254714938200064'
    >>> content.get_embed_code()
    "<div id='embedx-twt' align='center'></div><script async src='https://platform.twitter.com/widgets.js'></script><script> window.onload=(function(){twttr.widgets.createTweet(686254714938200064, document.getElementById('embedx-twt'),{});});</script>"

    """

    # pointer to current `OnlineContent` object
    instance = None

    # these templates must be defined by providing subclasses
    hostnames = []
    EMBED_SCRIPT = ""
    STATUS_LINK = ""  # it is needed for hosts which generate HTTP:200 even if CONTENT_ID is invalid e.g. Youtube
    LINK_TEMPLATE = ""  # not used. yet

    def __init__(self, url):
        # without protocol name, `urlparse` may not parse, so ...
        if not url.startswith('http'):
            url = 'http://' + url

        # URL-specific dispatching to `provider` objects e.g. Youtube, Twitter etc.
        for provider_obj in self.__class__.__subclasses__():
            _hosts = provider_obj.hostnames
            if any(x for x in _hosts if x in url):
                self.instance = provider_obj(url)

    def get_provider(self):
        return self.instance.__str__()

    def get_content_uid(self):
        """Returns the unique ID extracted from the link of the content
        """
        return self.instance.extract_id()

    def get_embed_code(self):
        if len(self.instance.EMBED_SCRIPT):
            return self.instance.EMBED_SCRIPT % ({'content_uid': self.get_content_uid()})
        elif len(self.instance.OEMBED_LINK):
            oembed_req_url = self.instance.EMBED_SCRIPT % ({'URL': self.instance.url})
        else:
            raise NotImplementedError

    def get_clean_link(self):
        if len(self.instance.LINK_TEMPLATE):
            return self.instance.LINK_TEMPLATE % ({'content_uid': self.get_content_uid()})
        else:
            raise NotImplementedError

    def extract_id(self):
        """Extract the unique ID from the URL link, set it to `self.content_uid`, and return the value.
        This method must be implemented by sub-class.
        :return: string ID of the content
        """
        raise NotImplementedError

    def check_if_alive(self):
        """Check if the content is available on the host server. Returns `True` if available, else `False`.
        This method is `lazy`-evaluated or only executes when called.
        :rtype: bool
        """
        from urllib2 import urlopen, URLError, HTTPError

        if len(self.instance.STATUS_LINK):
            check_url = self.instance.STATUS_LINK % ({'content_uid': self.get_content_uid()})
        else:
            # fallback
            check_url = self.instance.url

        try:
            response = urlopen(check_url)
        except (HTTPError, URLError):
            return False
        except ValueError:
            raise URLError('Invalid URL: %s'.format(check_url))
        else:
            return True if response.code == 200 else False


class YouTube(OnlineContent):
    hostnames = ['youtube', 'youtu.be']
    EMBED_SCRIPT = ("<div class='embedx-yt'>"
                    "<iframe src='http://www.youtube.com/embed/%(content_uid)s' 'frameborder='0' allowfullscreen>"
                    "</iframe></div>")
    STATUS_LINK = '''http://www.youtube.com/oembed?url=http://www.youtube.com/watch?v=%(content_uid)s&format=json'''
    LINK_TEMPLATE = '''https://www.youtube.com/watch?v=%(content_uid)s'''

    def __init__(self, url):
        self.url = url

    def extract_id(self):
        if '/channel/' in self.url:
            raise NotImplementedError

        if self.url.startswith(('youtu', 'www')):
            self.url = 'http://' + self.url
        parsed_url = urlparse(self.url)

        if 'youtube' in parsed_url.hostname:
            if parsed_url.path == '/watch':
                return parse_qs(parsed_url.query)['v'][0]
            elif parsed_url.path.startswith(('/embed/', '/v/')):
                return parsed_url.path.split('/')[2]
            else:
                raise NotImplementedError
        elif 'youtu.be' in parsed_url.hostname:
            return parsed_url.path[1:]
        else:
            raise ValueError


class Vimeo(OnlineContent):
    hostnames = ['vimeo', ]

    LINK_TEMPLATE = '''https://vimeo.com/%(content_uid)s'''
    STATUS_LINK = '''https://vimeo.com/api/oembed.json?url=https://vimeo.com/%(content_uid)s'''
    EMBED_SCRIPT = ("<div class='embedx-vm'>"
                    "<iframe src='http://player.vimeo.com/video/%(content_uid)s' "
                    "frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen>"
                    "</iframe></div>")

    def __init__(self, url):
        self.url = url

    def extract_id(self):
        if self.url.endswith('/'):
            return self.url.split('/')[-2]
        else:
            return self.url.split('/')[-1]


class Twitter(OnlineContent):
    hostnames = ['twitter', ]

    EMBED_SCRIPT = ("<div id='embedx-twt' align='center'></div>"
                    "<script async src='https://platform.twitter.com/widgets.js'></script>"
                    "<script> window.onload=(function(){twttr.widgets.createTweet(%(content_uid)s,"
                    " document.getElementById('embedx-twt'),{});});</script>")

    def __init__(self, url):
        self.url = url

    def extract_id(self):
        if '/status/' not in self.url:
            raise NotImplementedError
        else:
            return urlparse(self.url).path.split('/')[3]


class Github(OnlineContent):
    """
    Generate embed script for Github gist
    """
    hostnames = ['github', ]

    EMBED_SCRIPT = "<script src='https://gist.github.com/%(content_uid)s.js'></script>"

    def __init__(self, url):
        self.url = url

    def extract_id(self):
        if 'gist.' not in self.url:
            raise NotImplementedError
        else:
            return urlparse(self.url).path.split('/')[2]


class Flickr(OnlineContent):
    hostnames = ['flickr', ]

    # EMBED_SCRIPT = ""
    OEMBED_LINK = "https://www.flickr.com/services/oembed/?url=%(URL)s&format=json"

    def extract_id(self):
        raise NotImplementedError


class Facebook(OnlineContent):
    hostnames = ['facebook', 'fb.com']

    STATUS_LINK = ""
    EMBED_SCRIPT = ""

    def extract_id(self):
        raise NotImplementedError


if __name__ == '__main__':
    test_urls = ['https://twitter.com/thepodcastdude/status/686258030229336064',
                 'youtube.com/watch?v=_lOT2p_FCvA',
                 'https://www.facebook.com/kmonsoor/posts/10153282994792374',
                 'vimeo.com/150519302'
                 ]

    for a_url in test_urls:
        try:
            ov = OnlineContent(a_url)
            print ov.get_content_uid()
            # print ov.check_if_alive()
            print ov.get_embed_code()
        except NotImplementedError:
            pass
