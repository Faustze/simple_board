import os

from flask import Flask
from board.config import Config
from board.extensions import db, migrate
from board.context import make_shell_context
from dotenv import load_dotenv
from board import (
    extensions,
    errors,
    pages,
    posts,
)

import signal, sys


load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.logger.setLevel("INFO")

    db.init_app(app)
    migrate.init_app(app, db)

    from board import pages, posts
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_error_handler(404, errors.page_not_found)
    app.logger.debug(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    app.logger.debug(f"Using Database: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    
    from board import models

    app.shell_context_processor(make_shell_context)

    return app

def shutdown_handler(signum, frame):
    print('Server is shutting down...')
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown_handler)