# -*- coding:utf-8 -*-
# @Time : 2022/8/10 0:47
# @Author: Gendml
import json

import sqlalchemy
from flask import url_for, redirect, request, jsonify, make_response
from flask import Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setting import DB_URI
from utils.myutils import new_alchemy_encoder
from utils.relay import RelaySix
from utils.response import MyResponse
from sqlOperation import Silkworm

eq = Blueprint('equip', __name__, url_prefix='/equip/')
# 创建数据库引擎
engine = create_engine(DB_URI, echo=True)
# 获取session操作对象
Session = sessionmaker(bind=engine)
session = Session()


@eq.route('/queryRelayState/', methods=['GET'])
def hello_world():  # put application's code here
    relay = RelaySix(1, 1, 1, 1, 1, 1)
    res = MyResponse('一号继电器', 200, relay)
    return jsonify(res.to_dict())
    
@eq.route('/queryRelayState/', methods=['GET'])
def hello_world():  # put application's code here
    relay = RelaySix(1, 1, 1, 1, 1, 1)
    res = MyResponse('二号继电器', 200, relay)
    return jsonify(res.to_dict())




@eq.route('/queryone/', methods=['GET'])
def insertOne():
    result = session.query(Silkworm).all()
    if result is not None:
        res = MyResponse('查询数据库', 200, json.loads(json.dumps(result, cls=new_alchemy_encoder(), check_circular=False)))
        return jsonify(res.to_dict())
    return jsonify(MyResponse('查询数据库', 500, '').to_dict())

# @eq.route('/login/', methods=['GET', 'POST'])
# def login():  # put application's code here
#     name = request.args.get('name')
#     if not name:
#         redirect(url_for('hello_world'), code=301)
#     return name
