# -*- coding:utf-8 -*-
# @Time : 2022/8/9 21:36
# @Author: Gendml
import json

from utils.relay import RelaySix
from utils.response import MyResponse

if __name__ == '__main__':
    relay = RelaySix('OK', 'OK', 'OK', 'OK', 'OK', 'OK')
    # json.dumps()
    # 将python对象编码成Json字符串
    # json.loads()
    # 将Json字符串解码成python对象
    test = MyResponse('一号继电器', 200, relay)
    print(test)
