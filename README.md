[![License](https://img.shields.io/badge/license-MIT-blue.svg)](http://kmonsoor.mit-license.org/)

# extract-video-id
Extract Video ID from a video url

### Examples of URLs

####  Valid

    *  'http://youtu.be/_lOT2p_FCvA',
    *  'www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu',
    *  'http://www.youtube.com/embed/_lOT2p_FCvA',
    *  'http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US',
    *  'https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6',
    *  'youtube.com/watch?v=_lOT2p_FCvA',
      
####  Invalid:

    *  'youtu.be/watch?v=_lOT2p_FCvA'  (because Youtube don't give any url like this
    
## Install
    
    pip install git+https://github.com/kmonsoor/extract-video-id.git

## Usage

    from extract_video_id import youtube
    url = 'http://www.youtube.com/embed/_lOT2p_FCvA'
    video_id = youtube.get_video_id(url)


## To-do

* Create test
* Provision Travis-CI for automatic building & testing
* 

## Contributors

 * Intial version :  [Mikhail Kashkin](http://stackoverflow.com/users/85739/mikhail-kashkin)
 * Extension & projectization : [Khaled Monsoor](http://github.com/kmonsoor)
 * 

Please try to contribute by submitting more video sites as well as their different link formats. You can submit pull-requests or by creating issue.
