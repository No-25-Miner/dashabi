import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:toor123@127.0.0.1:3306/examination_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False




class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SEVER = 'smtp.googlemail.com'



class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    pass



config = {
 'development': DevelopmentConfig,
 'testing': TestingConfig,
 'production': ProductionConfig,
 'default': DevelopmentConfig
}