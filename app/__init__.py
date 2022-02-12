from flask import Flask
from config import Config
import pymysql
pymysql.install_as_MySQLdb()

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
db.drop_all()
migrate = Migrate(app,db)


login = LoginManager(app)
login.login_view = 'login'

from app import routes  #从app包中导入模块routes

#注：上面两个app是完全不同的东西。两者都是纯粹约定俗成的命名，可重命名其他内容。

