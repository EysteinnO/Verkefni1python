
from bottle import *
import os
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
    return "Þetta er gildi breytunnar tala", x

@error(404)
def villa(error):
    return "<h1>Þessi síða er ekki til</h1>"

run(host="0.0.0.0", port=os.environ.get('PORT'))


