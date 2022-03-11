# 一世无尘
# 倾尽温柔

# 数据库的连接配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zl_flask'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)