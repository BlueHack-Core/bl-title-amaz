from __future__ import print_function
from bl_title_amaz.title_filter import Title_filter
import re

api_instance = Title_filter()


filters = ['aaaa', 'bbb', 'ccc', 'ddd']
title = 'aaaa bbb bbb bbb bbb ccc ccc ddd ddd ddd'

for filter in filters:
    print(len(title))
    title = re.sub('\\b'+filter+' ' +'\\b', "", title)
    print(len(filter)+1)
    print(len(title))
    print(filter)
    print(title)
    print("##############")