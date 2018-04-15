


class Config(object):
    SECRET_KEY = 'ffd66034eab7718c1ed804eb18cb723d'
    RECAPTCHA_PUBLIC_KEY = '6LclUFMUAAAAADj5LAXMfuWuNukyKiA76tNCzG3K'
    RECAPTCHA_PRIVATE_KEY = '6LclUFMUAAAAANdw95wIbPP9tKxbic0NmQSc2OVB'



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://blog:blog123456@localhost:3306/blog'
    SQLALCHEMY_ECHO = True
    debug = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


