from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db
from webapp.user.models import User

app = create_app()

with app.app_context():
    username = input('Enter username:')

    if User.query.filter(User.username == username).count():
        print('User exists')
        sys.exit(0)

    password1 = getpass('Enter password: ')
    password2 = getpass('Retype pass: ')
    if not password1 == password2:
        print('Password incorrect')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с id {}'.format(new_user.id))
