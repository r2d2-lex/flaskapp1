from webapp import create_app
#from webapp.get_news import get_python_news
from webapp.news.parsers import habr


app = create_app()
with app.app_context():
    #habr.get_habr_snipperts()
    habr.get_news_content()
