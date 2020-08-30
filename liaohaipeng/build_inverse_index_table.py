# __author__ =  薯条老师
# __date__ = "2019-09-26"

import os
from . import  forward_matching_algorithm
import math
# 此函数为构建倒排索引表
def build_inverse_index_table(dataset_path):
    '''
    :return:返回倒排索引表
    '''
    inverse_index_table = {}

    WEB_PAGES = []
    for root, dirs, files in os.walk(dataset_path):
        for f in files:
            filename = os.path.join(root, f)
            content = open(filename, "r").read()
            WEB_PAGES.append({"filename": filename,
                              "content": content})

    web_pages_length = len(WEB_PAGES)
    '''
    在for循环中逐一遍历列表中的网页，内置函数enumerate可以返回列表的索引和值
    假设列表为['a','b','c'] 
    那么在for循环中通过enumerate函数遍历出的为如下索引值对:
    索引0，值'a',索引1，值'b'，索引2，值'c'，其它的同理
    '''
    for index, web_page in enumerate(WEB_PAGES):
        # 对web_page进行分词
        terms, terms_length = forward_matching_algorithm.cut(web_page["content"])
        for term in terms:
            # 计算term的tf值
            tf = round(terms[term] / terms_length, 4)
            page = {"filename": web_page["filename"], "tf": tf}
            if term not in inverse_index_table:
                inverse_index_table[term] = [page]
                continue
            # 如果term已存在于倒排表中，那么当前的term肯定是其它网页的term
            # 其它网页的term被添加进列表中，方便后续计算tf-idf
            inverse_index_table[term].append(page)

    for _, pages in inverse_index_table.items():
        terms_in_docs_length = len(pages)
        for page in pages:
            # 计算term的idf和tf-idf值
            page["idf"] = round(math.log10(web_pages_length / terms_in_docs_length)
                                , 4)
            page["tfidf"] = page["tf"] * page["idf"]

    return inverse_index_table