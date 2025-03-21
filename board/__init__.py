from flask import Flask
from board.config import Config
from board.extensions import db, migrate
from board.context import make_shell_context


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from board import pages, posts
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)

    from board import models

    app.shell_context_processor(make_shell_context)

    return app