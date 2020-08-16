#!/bin/sh
export FLASK_APP=webapp && flask db stamp head
flask db migrate -m "comments models addded"
FLASK_APP=webapp && flask db upgrade
