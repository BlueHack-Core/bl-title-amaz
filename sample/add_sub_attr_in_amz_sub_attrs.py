from __future__ import print_function
from pprint import pprint
from bl_title_amaz.title_filter import Title_filter

api_instance = Title_filter()

try:
    node_id = "5418126011"
    attr_id = "a0020"
    attr_kr_name = "attr 테스트"
    attr_us_name = "attr test"
    sub_attr_id = "aa0000000"
    sub_attr_kr_name = "sub attr 테스트"
    sub_attr_us_name = "sub attr test"
    res = api_instance.add_sub_attr_in_amz_sub_attrs(node_id, attr_id, attr_kr_name, attr_us_name,
                                                     sub_attr_id, sub_attr_kr_name, sub_attr_us_name)
    print("add sub_attr in amz_sub_attr DB is done!!")
    print(res)

except Exception as e:
    print("Exceptino when calling filtering_titles %s\n" % e)

