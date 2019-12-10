from flask import Flask, render_template
from webapp.model import db

from webapp.weather import wether_by_city
from webapp.get_news import get_python_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)

    @app.route('/')
    def index():
        weather = wether_by_city(app.config['WEATHER_CITY'])
        page_title = "Прогноз погоды"
        news_list = get_python_news()
        return render_template('index.html',weather=weather,page_title=page_title,news_list=news_list)
    return app
