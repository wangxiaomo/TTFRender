#-*- coding: utf-8 -*-

from TTFRender import generate, get_token_list


str = """
一
"""

token_list = get_token_list(str)
ttf_file   = "new.ttf"

generate(token_list, "kai", ttf_file)
