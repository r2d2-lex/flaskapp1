from flask import abort, Blueprint, flash, current_app, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from webapp import db
from webapp.news.forms import CommentForm
from webapp.weather import wether_by_city
from webapp.news.models import Comment, News
from webapp.utils import get_redirect_target

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

    comments_form = CommentForm(news_id=my_news.id)
    return render_template('news/view_one.html', page_title=my_news.title, news=my_news, comments_form=comments_form)


@blueprint.route('/news/comment', methods=['POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.comment_text.data, news_id=form.news_id.data, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Коментарий добавлен')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(form, field).label.text, error))
        print(form.errors)
        flash('Пожалуйста исправьте ошибки в форме')

    #return redirect(request.referrer)
    return redirect(get_redirect_target())
