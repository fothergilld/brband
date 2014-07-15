from flask import Flask
import jinja2

app = Flask(__name__)

@app.route("/")
def hello():
    return jinja2.FileSystemLoader(template_dir)

if __name__ == "__main__":
    app.config.from_object('config')
    with app.app_context():
        db.metadata.create_all(bind=db.engine)
    app.run()

