import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://user:password@localhost/ticket_management_db?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False