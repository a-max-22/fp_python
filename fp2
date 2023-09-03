
from pymonad.tools import *

@curry(2)
def tag(tagName, value):
	return '<'+tagName+'>'+value+'</'+tagName+'>' 
    
bold = tag('b')
italic = tag('i')

@curry(3)
def tag_ext(tagName, value, attr):
    attrs = ''
    for key in attrs:
        attrs += (key + '=' + attrs[key] + ' ')
    return '<' + tagName + ' ' + attrs + '>' + value+'</'+ tagName+'>' 

