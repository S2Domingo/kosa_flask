import os

#BASE_DIR = os.path.dirname(__file__)

DB_USER_NAME='admin'
DB_USER_PASSWD='password'
DB_HOST='dbhost'
DB_NAME='dbname'

SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}?charset=utf8'.format(DB_USER_NAME, DB_USER_PASSWD, DB_HOST, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False

