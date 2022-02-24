import logging

from flask import Flask
from config import Config
import pymysql
pymysql.install_as_MySQLdb()

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
db.drop_all()
migrate = Migrate(app,db)


login = LoginManager(app)
login.login_view = 'login'

mail = Mail(app)
bootstrap = Bootstrap(app)



if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler('logs/microblog.log',maxBytes=10240,backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Mircoblog startup')



from app import routes,models,errors  #从app包中导入模块routes

#注：上面两个app是完全不同的东西。两者都是纯粹约定俗成的命名，可重命名其他内容。

