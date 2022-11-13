# -*- coding:utf-8 -*-
# @Time : 2022/8/9 23:35
# @Author: Gendml
import json

CODE = {
    0: 'ON',
    1: 'OFF'
}


class RelaySix:
    def __init__(self, relay1, relay2, relay3, relay4, relay5, relay6):
        self.relay1 = CODE[relay1]
        self.relay2 = CODE[relay2]
        self.relay3 = CODE[relay3]
        self.relay4 = CODE[relay4]
        self.relay5 = CODE[relay5]
        self.relay6 = CODE[relay6]

    def __str__(self):
        return 'RelaySix(relay1=%s, relay2=%s, relay3=%s, relay4=%s, relay5=%s, relay6=%s)' \
               % (self.relay1, self.relay2, self.relay3, self.relay4, self.relay5, self.relay6)

    def __repr__(self):
        return self.__str__()
