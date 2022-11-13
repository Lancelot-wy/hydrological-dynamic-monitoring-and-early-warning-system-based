# -*- coding:utf-8 -*-
# @Time : 2022/8/11 16:15
# @Author: Gendml
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import Column, Integer, Float, DateTime, create_engine
from setting import DB_URI

# 创建数据库引擎
engine = create_engine(DB_URI, echo=True)
# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)
# 获取session操作对象
Session = sessionmaker(bind=engine)
session = Session()

# 创建ORM模型
class Silkworm(Base):
    # 定义表名
    __tablename__ = 'silkworm'

    # 配置字段
    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    nh3 = Column(Float, nullable=False)
    h2s=Column(Float,nullable=False)
    tvoc = Column(Float, nullable=False)
    co = Column(Float, nullable=False)
    time = Column(DateTime, nullable=False)

    def __init__(self, id, temperature, humidity, tvoc, nh3, h2s, co, time):
        self.id = id
        self.temperature = temperature
        self.humidity = humidity
        self.h2s = h2s
        self.tvoc = tvoc
        self.nh3 = nh3
        self.co = co
        self.time = time

    # 让打印出来的数据更好看，可选的
    def __repr__(self):
        return '<Silkworm(id = %s, temperature = %s, humidity = %s, tvoc = %s, nh3 = %s, h2s = %s, co = %s, time = %s)>' \
               % (self.id, self.temperature, self.humidity,  self.tvoc, self.nh3, self.h2s, self.co, self.time)

    def __str__(self):
        return self.__repr__()



# 将模型映射到数据库中
Base.metadata.create_all()

if __name__ == '__main__':
    # 增加一条数据
    object = Silkworm(id=None, temperature=1.0, humidity=1.0, tvoc=1.0, nh3=1.0, h2s=1.0, co=1.0, time=datetime.now())
    print(object)
    session.add(object)
    # session.rollback()
    session.commit()

    # # 查询数据 -> 使用all()返回一个对象列表
    # res = session.query(Silkworm).all()
    # print(res)