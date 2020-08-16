from flask import abort, Blueprint, current_app, render_template
from webapp.news.forms import CommentForm
from webapp.weather import wether_by_city
from webapp.news.models import News


blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    weather = wether_by_city(current_app.config['WEATHER_CITY'])
    page_title = "Прогноз погоды"
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    print(news_list)
    return render_template('news/index.html', weather=weather, page_title=page_title, news_list=news_list)


@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()
    if not my_news:
        abort(404)

    comment_form = CommentForm(news_id=my_news.id)
    return render_template('news/view_one.html', page_title=my_news.title, news=my_news, comments_form=comment_form)


@blueprint.route('/news/comment', methods=['POST'])
def add_comment():
    pass
