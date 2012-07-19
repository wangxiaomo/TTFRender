#-*- coding: utf-8 -*-

"""
Some Helper Function of Module TTFRender
"""

import os
import re

#TODO: Make a Adapter to Get the TTF FILE of Specified Font
def get_ttf_file(font_name):
    FONT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))+"/fonts/"
    return _unicode(FONT_DIRECTORY+"钟齐吴嘉睿手写字.ttf")

# Get the Unicode of Specified Word
def _unicode(w):
    if isinstance(w, unicode):
        return w
    else:
        return w.decode("utf-8")

# Get The Token List of a Sentence
def get_token_list(line):
    line = _unicode(line)
    return list(set(re.findall(r'\w|\W', line)))
