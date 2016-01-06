from urlparse import urlparse, parse_qs

from .online_video import OnlineVideo


class YouTube(OnlineVideo):
    valid_hostnames = ['youtube', 'youtu.be']
    EMBED_SCRIPT = '''<div class='embed-container'><iframe src='http://www.youtube.com/embed/%(VIDEO_ID)s '
                      'frameborder='0'allowfullscreen></iframe></div>'''
    STATUS_LINK = '''http://www.youtube.com/oembed?url=http://www.youtube.com/watch?v=%(VIDEO_ID)s&format=json'''
    LINK_TEMPLATE = '''https://www.youtube.com/watch?v=%(VIDEO_ID)s'''

    def __init__(self):
        if not any([x for x in self.valid_hostnames if x in self.url]):
            raise ValueError('Invalid URL for a Youtube video')
        self.video_id = self.extract_id()
        self.is_alive = None

    def extract_id(self):
        """Returns Video_ID extracting from the given url of Youtube

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
                self.video_id = parse_qs(parsed_url.query)['v'][0]
            elif parsed_url.path.startswith(('/embed/', '/v/')):
                self.video_id = parsed_url.path.split('/')[2]
        elif 'youtu.be' in parsed_url.hostname:
            self.video_id = parsed_url.path[1:]
        else:
            raise ValueError
