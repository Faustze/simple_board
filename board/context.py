import sqlalchemy as sa
import sqlalchemy.orm as so
from board.extensions import db
from board.models import Post

def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'Post': Post}