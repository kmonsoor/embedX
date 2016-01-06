[![License](https://img.shields.io/badge/license-MIT-blue.svg)](http://kmonsoor.mit-license.org/)

# extract-video-id
Extract Video ID from a video url and provides different codes from there.

### Currently, supports

 * Youtube
 * Vimeo



### Examples of URLs

####  Valid

 *  'http://youtu.be/_lOT2p_FCvA',
 *  'www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu',
 *  'http://www.youtube.com/embed/_lOT2p_FCvA',
 *  'http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US',
 *  'https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6',
 *  'youtube.com/watch?v=_lOT2p_FCvA',
 *  'https://vimeo.com/groups/animation/videos/150618894/'
 *  'https://vimeo.com/150519302'
 *  etc.
      
####  Invalid:

 * 'youtu.be/watch?v=_lOT2p_FCvA'  [ because Youtube don't give any url like this ]
    
## Install

### Directly from source
    
    pip install git+https://github.com/kmonsoor/extract-video-id.git


## Usage

    >>> from online_video import OnlineVideo
    >>> ov = OnlineVideo('http://www.youtube.com/embed/_lOT2p_FCvA')
    >>> ov.get_video_id()
    '_lOT2p_FCvA'
    
    >>> ov.get_embed_code()
    "<div class='embed-container'><iframe src='http://www.youtube.com/embed/_lOT2p_FCvA' 'frameborder='0'allowfullscreen></iframe></div>"
    
    >>> ov = OnlineVideo('https://vimeo.com/groups/animation/videos/150618894/')
    >>> ov.get_embed_code()
    "<div class='embed-container'> <iframe src='http://player.vimeo.com/video/150618894' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>"
    


## To-do

* Create test
* Provision Travis-CI for automatic building & testing
* 

## Contributors

 * Seed idea :  [A StackOverflow answer](http://stackoverflow.com/a/7936523) by [Mikhail Kashkin](http://stackoverflow.com/users/85739/mikhail-kashkin)
 * Author : [Khaled Monsoor](http://github.com/kmonsoor)
 * 

Please try to contribute by submitting more video sites as well as their different link formats. You can submit pull-requests or by creating issue.
