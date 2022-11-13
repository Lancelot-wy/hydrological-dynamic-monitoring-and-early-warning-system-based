# -*- coding:utf-8 -*-
# @Time : 2022/8/11 22:33
# @Author: Gendml
# 数据库的配置变量
from sqlalchemy import create_engine



HOSTNAME = '192.168.31.11'
PORT = '3306'
DATABASE = 'silkworm_db'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)


