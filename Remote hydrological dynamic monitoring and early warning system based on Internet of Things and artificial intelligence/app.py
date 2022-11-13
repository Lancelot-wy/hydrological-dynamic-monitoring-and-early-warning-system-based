#!/bin/bash/python
# -*- coding: utf-8 -*-
from flask_restful import Api, Resource
from flask import Flask, make_response, jsonify
import equipmentControl

app = Flask(__name__)
# 用Api来绑定app
api = Api(app)
# 注册蓝图
app.register_blueprint(equipmentControl.eq)


@app.route("/", methods=["GET", "POST"])
def index():
    return 'Flask has been run successfully.'


@app.errorhandler(404)
def no_found(error):
    return make_response(jsonify())


if __name__ == '__main__':
    app.run(host='192.168.31.11', port=80, debug=True)
