from __future__ import print_function
from pprint import pprint
from bl_title_amaz.title_filter import Title_filter

api_instance = Title_filter()

try:
    # 1분정도 소요됨ㅠㅠ
    node_ids = ["2368343011", "2368365011"]
    res = api_instance.get_title_word_dic_by_node_id(node_ids)
    print("get title dic done!")
    print(res)

except Exception as e:
    print("Exceptino when calling filtering_titles %s\n" % e)

