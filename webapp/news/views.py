from flask import Blueprint, render_template, current_app
from webapp.weather import wether_by_city
from webapp.news.models import News


blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    weather = wether_by_city(current_app.config['WEATHER_CITY'])
    page_title = "Прогноз погоды"
    news_list = News.query.order_by(News.published.desc()).all()
    print(news_list)
    return render_template('index.html', weather=weather, page_title=page_title, news_list=news_list)
