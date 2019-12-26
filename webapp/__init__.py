from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user
from webapp.model import db, News, User

from webapp.forms import LoginForm
from webapp.weather import wether_by_city
#from webapp.get_news import get_python_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        weather = wether_by_city(app.config['WEATHER_CITY'])
        page_title = "Прогноз погоды"
        news_list = News.query.order_by(News.published.desc()).all()
        print(news_list)
        return render_template('index.html',weather=weather,page_title=page_title,news_list=news_list)

    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username = form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы вошли на сайт')
                return redirect(url_for('index'))

        flash('Неверное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы разлогинились')
        return redirect(url_for('index'))

    return app
