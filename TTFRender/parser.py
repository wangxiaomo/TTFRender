#-*- coding: utf-8 -*-

"""
Parse the TTF FILE && Generate a New TTF FILE
"""

try:
    import fontforge
except ImportError:
    raise ImportError("Need Module fontforge!")


from helper import get_ttf_file
from helper import _unicode

def generate(token_list, font_name, filename):
    """ Generate the TTF FILE of Specified Font """
    font_file = get_ttf_file(font_name)
    fnt = fontforge.open(font_file)
    for w in fnt.glyphs():
        if w.unicode<0 or \
                (unichr(w.unicode) not in map(lambda x:_unicode(x), token_list)):
            fnt.removeGlyph(w)
        else:
            print unichr(w.unicode)

    fnt.generate(filename)
    fnt.close()
