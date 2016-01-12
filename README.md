[![License](https://img.shields.io/badge/license-MIT-blue.svg)](http://kmonsoor.mit-license.org/)

# embedX

Generate embeddable HTML or JavaScript code for a online content from its URL in a single step. 

The content can be:
 * Yotube video
 * Twitter status
 * Vimeo video
 * 
 etc.

 
Embeddable code-generation be simple like this: 

    >>> from embed_x import OnlineContent
    >>> oc = OnlineContent('http://www.youtube.com/embed/_lOT2p_FCvA')
    >>> oc.get_embed_code()
    "<div class='embedx-yt'><iframe src='http://www.youtube.com/embed/_lOT2p_FCvA' 'frameborder='0' allowfullscreen></iframe></div>"
    
    

### Currently, supports

 * Youtube video
 * Vimeo video
 * Twitter : single status
 * 



### Examples of URLs

####  Valid

 *  http://youtu.be/_lOT2p_FCvA
 *  www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu
 *  http://www.youtube.com/embed/_lOT2p_FCvA
 *  http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US
 *  https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6
 *  youtube.com/watch?v=_lOT2p_FCvA
 *  https://vimeo.com/groups/animation/videos/150618894/
 *  https://vimeo.com/150519302
 *  https://twitter.com/codinghorror/status/686254714938200064
 * 
      
####  Invalid:

 * youtu.be/watch?v=_lOT2p_FCvA  [ because Youtube don't give any url like this ]
 * https://twitter.com/gvanrossum/with_replies
 * 
 
  
    
## Install

### from PyPI

    pip install embedX

### Directly from source

    pip install git+https://github.com/kmonsoor/embedX.git
    


## Usage

    >>> from online_video import OnlineVideo
    >>> oc = OnlineVideo('http://www.youtube.com/embed/_lOT2p_FCvA')
    >>> oc.get_video_id()
    '_lOT2p_FCvA'

    >>> oc.get_embed_code()

    "<div class='embed-container'><iframe src='http://www.youtube.com/embed/_lOT2p_FCvA' 'frameborder='0'allowfullscreen></iframe></div>"

    >>> oc = OnlineVideo('https://vimeo.com/groups/animation/videos/150618894/')
    >>> oc.get_embed_code()
    "<div class='embed-container'> <iframe src='http://player.vimeo.com/video/150618894' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>"
    


## To-do

* Create test
* Provision Travis-CI for automatic building & testing
* add more content sites
  * Github gists
  * Facebook status
  * Facebook notes
  * Scribd docs
  * Imgur images
  

## Contributors

 * Seed idea :  [A StackOverflow answer](http://stackoverflow.com/a/7936523) by [Mikhail Kashkin](http://stackoverflow.com/users/85739/mikhail-kashkin)
 * Author : [Khaled Monsoor](http://github.com/kmonsoor)
 * 

Please try to contribute by submitting more content-sites with their different link formats and embed-codes. You can submit pull-requests or by creating issue.
