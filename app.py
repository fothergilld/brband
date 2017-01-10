import os

from flask import Flask, redirect, request, render_template
from flaskext.markdown import Markdown
import yaml

app = Flask(__name__)
md = Markdown(app)

# redirect_urls = {
#     '/old/': '/'
# }

# def redirect_url():
#     return redirect(redirect_urls[request.url], 301)

# for url in redirect_urls:
#     app.add_url_rule(url, url, redirect_url)

@app.route('/')
def show_entries():
    posts = yaml.load(file('content/posts.yaml', 'r'))
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run()
