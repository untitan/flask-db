# mysql+pymysql://cls:cls123@192.168.66.13/clsdb

DIALECT = 'mysql'   #指定数据库
DRIVER = 'pymysql'  #pymysql驱动
USERNAME = 'pp'
PASSWORD = 'pp123'
HOST = '192.168.66.13'
PORT = '3306'
DATABASE = 'ppdb'

#数据库连接
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

#是否创建数据库
IS_CREATE_DB = False

#debug方式启动
DEBUG = True
