# -*- coding:utf-8 -*-
# @Time : 2022/8/9 22:50
# @Author: Gendml
import json

CODE = {
    200: 'SUCCESS',
    500: 'FAILURE',
}


class MyResponse:
    def __init__(self, name, code, data):
        self.name = name
        self.code = code
        self.msg = CODE[code]
        self.data = data

    def __str__(self):
        return 'MyResponse(name=%s, code=%s, msg=%s, data=%s)' % (self.name, self.code, self.msg, self.data)

    def __repr__(self):
        return self.__str__()

    # 将response深度转为dict后 再转回字典返回
    def to_dict(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False))

