
# from bull import app
import os
import jinja2
from os.path import abspath, dirname, join
from flask import Flask, redirect, request, render_template

template_loc = os.path.abspath(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'templates'))

static_folder = os.path.abspath(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'static'))

my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader(template_loc),
])
app.jinja_loader = my_loader

redirect_urls = {
    '/old/': '/'
}

app = Flask(__name__)

def redirect_url():
    return redirect(redirect_urls[request.url], 301)

for url in redirect_urls:
    app.add_url_rule(url, url, redirect_url)

@app.route('/')
def show_entries():
  return render_template('splash.html')

# def show_entries():
#     db = get_db()
#     cur = db.execute('select title, text from entries order by id desc')
#     entries = cur.fetchall()
#     return render_template('show_entries.html', entries=entries)

def get_app():
    return app

if __name__ == '__main__':
    app.config.from_object('config')
    # with app.app_context():
    #     db.metadata.create_all(bind=db.engine)
    get_app().run(debug=True)
    # get_app().run(host='127.13.48.2', port=15000,debug=True)
    #get_app().run(debug=True, static_folder=static_folder)
