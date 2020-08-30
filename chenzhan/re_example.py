import re
'''
url = 'http://www.123.org/'
result = re.match("^http://(.*(com|cn|org))/?", url)

print(result.group(1))
'''


email = '12334343chenzhan@sohu.com'
"""
(1) QQ邮箱的格式：123456@qq.com
(2) 网易邮箱的格式：12334343@163.com 或 12311234@126.com
(3) 新浪邮箱的格式：12334343@sina.com 或 sina.cn
(4) 搜狐邮箱的格式：12334343@sohu.com
"""


pattern = "^\w{6,}@(.{5,}(com|cn))"
result = re.match(pattern, email)
print(result.group(1))