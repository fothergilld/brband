from os.path import abspath, dirname, join
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

redirect_urls = {
    '/old/': '/'
}

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
    app.run()
