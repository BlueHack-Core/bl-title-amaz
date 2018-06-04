from __future__ import print_function
from pprint import pprint
from bl_title_amaz.title_filter import Title_filter

api_instance = Title_filter()

try:
    node_ids = ["2368343011"]
    filter = api_instance.get_title_word_dic_by_node_id(node_ids)

    filtered_titles, result_word = api_instance.filtering_titles(node_ids, filter)
    print("filtering title done!")
    for dic in filtered_titles:
        print(dic)

    print(result_word)

except Exception as e:
    print("Exception when calling filtering_titles %s\n" % e)

