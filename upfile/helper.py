"""

"""
import datetime
import random

"""
对文件上传的名字重命名
"""
IMG_PREFIX_NAME = 'IMG'


# 1.jpg 2.png
def get_file_name(file_name):
    suffix_name = '.' + file_name.split('.')[-1]
    # 时间 + 随机数
    new_name = IMG_PREFIX_NAME \
               + (datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + str(random.randint(10000, 99999))

    return new_name + suffix_name
