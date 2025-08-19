import os

class Config:
    DB_USER = os.getenv('DB_USER', 'user')
    DB_PASS = os.getenv('DB_PASS', 'password')
    DB_NAME = os.getenv('DB_NAME', 'meubanco')
    DB_HOST = os.getenv('DB_HOST', 'db')
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False