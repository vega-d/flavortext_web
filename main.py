import os
from flask import Flask, render_template, send_from_directory
from utils import *
from flask_restful import Api

app = Flask(__name__)

api = Api(app)
api.add_resource(API_point, '/api')


def main():
    # db_session.global_init("db/blogs.sqlite")
    # app.register_blueprint(api_files.blueprint)

    app.run(
        port=1400,
        # host=gv.host
    )


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join('static', 'img'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/robots.txt')
def robots():
    return send_from_directory("templates", "robots.txt")


@app.route("/plain")
def curl():
    return generate_phrase()


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def graphical():
    return render_template("gui.html", text=generate_phrase())


if __name__ == '__main__':
    main()
