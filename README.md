[![License](https://img.shields.io/badge/license-MIT-blue.svg)](http://kmonsoor.mit-license.org/)
[![PyPI version](https://badge.fury.io/py/embedX.svg)](https://badge.fury.io/py/embedX)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/69f2bf7e3b404e6c90015053e48a1cbf/badge.svg)](https://www.quantifiedcode.com/app/project/69f2bf7e3b404e6c90015053e48a1cbf)

# embedX

Generate embeddable HTML or JavaScript code for a online content from its URL in a single step.

The content can be anything like 

 * Youtube or Vimeo video,
 * Twitter status,
 * Github Gist,
 etc.


Embeddable code-generation be simple like this:

    >>> from embed_x import OnlineContent
    >>> oc = OnlineContent('http://www.youtube.com/embed/_lOT2p_FCvA')
    >>> oc.get_embed_code()
    "<div class='embedx-yt'><iframe src='http://www.youtube.com/embed/_lOT2p_FCvA' 'frameborder='0' allowfullscreen></iframe></div>"

    

### Currently, supports

 * Youtube video,
 * Vimeo video,
 * Twitter: single status,
 * Github gist,
 * Flickr image



### Examples of URLs

####  Valid

 *  http://youtu.be/_lOT2p_FCvA
 *  www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu
 *  http://www.youtube.com/embed/_lOT2p_FCvA
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

    pip install embedx

### Directly from source

    pip install git+https://github.com/kmonsoor/embedX.git

## Requirements
    
    This library don't have any external dependencies other than standard Python installation.


## Usage

    >>> from embedx import OnlineContent
    >>> oc = OnlineContent('http://www.youtube.com/embed/_lOT2p_FCvA')
    >>> oc.extract_id()
    '_lOT2p_FCvA'

    >>> oc.get_embed_code()
    "<div class='embed-container'><iframe src='http://www.youtube.com/embed/_lOT2p_FCvA' 'frameborder='0'allowfullscreen></iframe></div>"

    >>> oc = OnlineContent('https://vimeo.com/groups/animation/videos/150618894/')
    >>> oc.get_embed_code()
    "<div class='embed-container'> <iframe src='http://player.vimeo.com/video/150618894' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>"



## To-do

* Create test cases for automated testing
* Provision Travis-CI for automatic building & testing
* Add support for [conda](http://conda.pydata.org/docs/index.html)-based installation
* Add more rich-content sites

  - [x] Github gists
  - [ ] Facebook status
  - [ ] Facebook notes
  - [ ] Scribd docs
  - [ ] Imgur images


## Contributors

 * Seed idea :  [A StackOverflow answer](http://stackoverflow.com/a/7936523) by [Mikhail Kashkin](http://stackoverflow.com/users/85739/mikhail-kashkin)
 * Author : [Khaled Monsoor](http://github.com/kmonsoor)
 * 

Please try to contribute by submitting more content-sites with their different link formats and embed-codes. You can submit through pull-requests or by creating issue.
