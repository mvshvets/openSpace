from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from app.app import ns

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, supports_credentials=True)

api = Api(app, version='1.0', title='Test API',
          description='Простая тестовая демонстрация работы API')
api.add_namespace(ns)
