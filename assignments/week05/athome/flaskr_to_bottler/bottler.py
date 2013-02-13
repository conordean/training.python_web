import sqlite3
from contextlib import closing

from bottle import Bottle
from bottle import default_app
from bottle import error
from bottle import get
from bottle import install
from bottle import post
from bottle import redirect
from bottle import request
from bottle import static_file
from bottle import TEMPLATE_PATH
from bottle import url
from bottle import jinja2_template as template

from bottle_sqlite import SQLitePlugin
from bottle_flash import FlashPlugin

# configuration goes here
DATABASE = '/tmp/bottler.db'
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Bottle(__name__)

# Resource configuration (relative to current file)
app.resources.add_path('./', base=__file__)
TEMPLATE_PATH.append("./templates")

app.install(SQLitePlugin(dbfile='/tmp/bottler.db'))
app.install(FlashPlugin(secret='COOKIE_SECRET'))

def connect_db():
    return sqlite3.connect('/tmp/bottler.db')


def init_db():
    with closing(connect_db()) as db:
        with app.resources.open('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

#@app.before_request
#def before_request():
#    g.db = connect_db()


#@app.teardown_request
#def teardown_request(exception):
#    g.db.close()

def write_entry(title, text):
    db.execute('insert into entries (title, text) values (?, ?)',
               [title, text])
    db.commit()


def get_all_entries():
    db = connect_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return entries

@app.route('/')
def show_entries():
    db = connect_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return template('show_entries.html', entries=entries) 

##############################################################
# TEST PASS
#
#@app.route('/')
#@app.route('/hello/<name>')
#def greet(name='Stranger'):
#    return template('home.html', name=name)
##############################################################

@app.route('/add', methods=['POST'])
def add_entry():
    try:
        write_entry(request.form['title'], request.form['text'])
        flash('New entry was successfully posted')
    except sqlite3.Error as e:
        flash('There was an error: %s' % e.args[0])
    return redirect(url('show_entries'))


if __name__ == '__main__':
    app.run(debug=True)
