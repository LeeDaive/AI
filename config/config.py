import os
import dotenv

dotenv.load_dotenv()

DEFAULT = {
    'DB_USERNAME': 'postgres',
    'DB_PASSWORD': 'root',
    'DB_PORT': '5432',
    'DB_HOST': '127.0.0.1',
    'DB_DATABASE': 'ai',
    'SQLALCHEMY_POOL_SIZE': 30,
    'SQLALCHEMY_ECHO': 'False',
    'LOG_LEVEL': 'INFO',
    'CORPID': 'wwa921b0843fcc7548',
    'CORPSECRET': 'SIHMdN4P-umrZM4xfH6y9pQFL4ynjQYK3m6WkJGD9yE'
}

def get_env(key):
    return os.environ.get(key, DEFAULT.get(key))

class Config:

    def __init__(self):
        db_credentials = {
            key: get_env(key) for key in ['DB_USERNAME', 'DB_PASSWORD', 'DB_PORT', 'DB_HOST', 'DB_DATABASE']
        }
        self.SQLALCHEMY_DATABASE_URI = f"postgresql://{db_credentials['DB_USERNAME']}:{db_credentials['DB_PASSWORD']}@{db_credentials['DB_HOST']}:{db_credentials['DB_PORT']}/{db_credentials['DB_DATABASE']}"
        self.SQLALCHEMY_ENGINE_OPTIONS = {'pool_size': int(get_env('SQLALCHEMY_POOL_SIZE'))}
