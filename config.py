import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

basedir = Path(__file__).parent

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{basedir/"instance"/"site.db"}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False