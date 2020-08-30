# __author__ =  薯条老师
# __date__ = "2019-09-26"


import config

def cut(text):
    '''
    :param text:待分词的文本
    :return:返回分词结果词典，分词数
    '''
    words = {}
    words_length = 0
    # 将text变量作为判断条件，如果text为空值，则停止循环
    # 在循环中会不断将text变量进行切片
    while text:
        # 定义word_not_in_dictionary布尔类型变量，用来判断是否分词成功
        word_not_in_dictionary = True
        # 执行range函数会生成一个整数序列，
        # 读者可以查阅官方文档，来了解range函数的用法
        # 这里的range函数为生成一个倒排序列，比如6,5,4,3,2,1
        for index in range(config.THE_MAX_LENGTH_OF_WORD, 0, -1):
            # 对文本按最大宽度进行切片
            word = text[:index]
            # 如果切片分出来的词语在词典集合中，就保存到列表words变量中，并且退出for循环
            # 在集合中进行快速查找
            if word in config.DICTIONARY:
                words_length += 1
                words[word] = 1 if word not in words else words[word] + 1
                text = text[index:]
                word_not_in_dictionary = False
                break

        if word_not_in_dictionary:
            # 如果匹配失败，则将文本的起始位置向前移动一个位置，重复进行上述的分词步骤
            text = text[1:]

    return words, words_length
