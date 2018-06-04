from __future__ import print_function
from pprint import pprint
from bl_title_amaz.title_filter import Title_filter

api_instance = Title_filter()

try:
    sub_attr_id = "aa0000001"
    sub_attr_word = "test"
    res = api_instance.add_sub_attr_word_in_amz_title_dic(sub_attr_id, sub_attr_word)
    print("add sub_attr_word in amz_title_dic DB is done!!")
    print(res)

except Exception as e:
    print("Exceptino when calling filtering_titles %s\n" % e)

