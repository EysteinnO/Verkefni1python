# -*- coding: cp1252 -*-
from bottle import *

@route('/')
def index():
    return '''
          <div>
          <a href='/sida/about'>About</a> </b><a href='/sida/bio'>Biography</a> <a href='/sida/pic'>Pictures</a>
          </div>
          '''

@route('/sida/<id>')
def index(id):
    return "Her er ", id, " sidan"

def about():
    return "Hallo hesugndjonk"

@route('/gaman')
def index():
    x = request.query.tala
    return "�etta er gildi breytunnar tala", x

@error(404)
def villa(error):
    return "<h1>�essi s��a er ekki til</h1>"
run(host="localhost", port=8080);
