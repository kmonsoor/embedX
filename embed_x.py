from urlparse import urlparse, parse_qs


class OnlineContent(object):
    url = None
    content_uid = None
    instance = None

    # these templates must be defined by providing subclasses
    EMBED_SCRIPT = ''''''
    LINK_TEMPLATE = ''''''
    STATUS_LINK = ''''''

    def __init__(self, url):
        self.url = url
        # URL-specific dispatching to `provider` objects e.g. Youtube, Vimeo etc.
        for provider_obj in self.__class__.__subclasses__():
            _hosts = provider_obj.get_hostnames()
            if any( x for x in _hosts if x in url):
                self.instance = provider_obj(self.url)
                self.content_uid = self.get_content_uid()

    def get_provider(self):
        return self.instance.__str__()

    def get_content_uid(self):
        """Returns the unique ID extracted from the link of the content
        """
        self.content_uid = self.instance.extract_id()
        return self.content_uid

    def get_embed_code(self):
        if self.content_uid is None:
            self.instance.extract_id()
        if len(self.instance.EMBED_SCRIPT) > 0:
            return self.instance.EMBED_SCRIPT % ({'content_uid': self.content_uid})
        else:
            raise NotImplementedError

    def get_clean_link(self):
        if self.content_uid is None:
            self.instance.extract_id()
        if len(self.instance.LINK_TEMPLATE) > 0:
            return self.instance.LINK_TEMPLATE % ({'content_uid': self.content_uid})
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

        if not len(self.instance.STATUS_LINK):
            raise NotImplementedError
        url = self.instance.STATUS_LINK % ({'content_uid': self.content_uid})
        try:
            response = urlopen(url)
        except (HTTPError, URLError):
            return False
        except ValueError:
            raise URLError('Invalid URL: %s'.format(url))
        else:
            return True if response.code == 200 else False


class YouTube(OnlineContent):
    # hostnames = ['youtube', 'youtu.be']
    EMBED_SCRIPT = '''<div class='embed-container'><iframe src='http://www.youtube.com/embed/%(content_uid)s'
                      'frameborder='0'allowfullscreen></iframe></div>'''
    STATUS_LINK = '''http://www.youtube.com/oembed?url=http://www.youtube.com/watch?v=%(content_uid)s&format=json'''
    LINK_TEMPLATE = '''https://www.youtube.com/watch?v=%(content_uid)s'''

    @staticmethod
    def get_hostnames():
        return ['youtube', 'youtu.be']

    def __init__(self, url):
        self.url = url

    def extract_id(self):
        """Returns content_uid extracting from the given url of Youtube

        Examples of URLs:
          Valid:
          'http://youtu.be/_lOT2p_FCvA',
          'www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu',
          'http://www.youtube.com/embed/_lOT2p_FCvA',
          'http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US',
          'https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&'\
                          list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6',
          'youtube.com/watch?v=_lOT2p_FCvA',

          Invalid:
            'youtu.be/watch?v=_lOT2p_FCvA',
        """

        if self.url.startswith(('youtu', 'www')):
            self.url = 'http://' + self.url
        parsed_url = urlparse(self.url)

        if 'youtube' in parsed_url.hostname:
            if parsed_url.path == '/watch':
                return parse_qs(parsed_url.query)['v'][0]
            elif parsed_url.path.startswith(('/embed/', '/v/')):
                return parsed_url.path.split('/')[2]
        elif 'youtu.be' in parsed_url.hostname:
            return parsed_url.path[1:]
        else:
            raise ValueError


class Vimeo(OnlineContent):
    LINK_TEMPLATE = '''https://vimeo.com/%(content_uid)s'''
    STATUS_LINK = '''https://vimeo.com/api/oembed.json?url=https://vimeo.com/%(content_uid)s'''
    EMBED_SCRIPT = '''<div class='embed-container'> <iframe src='http://player.vimeo.com/video/%(content_uid)s' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>'''

    @staticmethod
    def get_hostnames():
        return ['vimeo', ]

    def __init__(self, url):
        self.url = url

    def extract_id(self):
        if self.url.endswith('/'):
            return self.url.split('/')[-2]
        else:
            return self.url.split('/')[-1]


if __name__ == '__main__':
    ov = OnlineContent(url='https://vimeo.com/groups/animation/videos/150618894/')

    print ov.get_content_uid()
    print ov.check_if_alive()
    print ov.get_embed_code()
