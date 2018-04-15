# -*- coding: utf-8 -*-

from flask import (
    Flask,
    redirect,
    url_for
)

from Blog.config import DevConfig

from Blog.models.blogs import db

from Blog.contrellors.blogs import blog_blueprint

from Blog.models.extensions import bcrypt





def create_app(object_name):
    app = Flask(__name__)

    app.config.from_object(object_name)

    db.init_app(app)
    bcrypt.init_app(app)

    @app.route("/")
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blog_blueprint)
    return app





if __name__ == '__main__':
    create_app().run(host='127.0.0.1', port=3000)



