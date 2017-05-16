import os

from flask import Flask, redirect, request, render_template
from flaskext.markdown import Markdown
import yaml
from chalice import Chalice

app = Chalice(app_name='brband')

#app = Flask(__name__)
md = Markdown(app)

@app.route('/')
def show_entries():
    posts = yaml.load(file('content/posts.yaml', 'r'))
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run()
