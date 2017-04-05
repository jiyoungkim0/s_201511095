
# coding: utf-8

# In[14]:



import lxml.html
import requests

keyword='순정에 반하다'
req = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
_html = lxml.html.fromstring(req.text)


from lxml.cssselect import CSSSelector
selec = CSSSelector('table[summary] > tbody > ._tracklist_move')
nodes = selec(_html)

_songName = CSSSelector('.name > a.title')
_songArtist = CSSSelector('._artist.artist')
_songAlbum= CSSSelector('.album > a')
for node in nodes:
    _name=_songName(node)
    _artist=_songArtist(node)
    _album=_songAlbum(node)
    if _name:
        print _artist[0].text_content().strip(),
        print "/",
        print _name[0].text_content(),
        print "/",
        print _album[0].text_content()

