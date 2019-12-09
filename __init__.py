from flask import Flask, render_template
from weather import wether_by_city
from get_news import get_python_news
from model import db

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)

@app.route('/')

def index():
    weather = wether_by_city("Chelyabinsk, Russia")
    page_title = "Прогноз погоды"
    news_list = get_python_news()
    return render_template('index.html',weather=weather,page_title=page_title,news_list=news_list)


if __name__ == '__main__':
    app.run(debug=True)

