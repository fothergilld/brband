
from bull import app, db
import os
import jinja2
from os.path import abspath, dirname, join
from flask import Flask, redirect, request

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

def redirect_url():
    return redirect(redirect_urls[request.url], 301)

for url in redirect_urls:
    app.add_url_rule(url, url, redirect_url)



def get_app():
    return app

if __name__ == '__main__':
    app.config.from_object('config')
    with app.app_context():
        db.metadata.create_all(bind=db.engine)
    #get_app().run(host='127.13.48.2', port=15000,debug=True)
    get_app.run(debug=True, static_folder=static_folder)
