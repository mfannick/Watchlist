import os
class Config:
    '''
    General configuration parent class
    '''
    
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    
    MOVIE_API_KEY='c2718abd682cdb4218184e8c0ad1028a'
    
    SECRET_KEY ='Fannick1'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://annick:annick12@@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

     #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://annick:annick12@@localhost/watchlist_test'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://annick:annick12@@localhost/watchlist'
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
 
