import sqlalchemy as sa

from flask import (
    Blueprint, 
    render_template, 
    redirect, 
    request, 
    url_for,
)
from board.extensions import db
from board.models import Post


bp = Blueprint('posts', __name__)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        author = request.form.get('author','Anonymous')
        message = request.form.get('message')

        if message:
            new_post = Post(author=author, message=message)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('posts.posts'))
        
    return render_template('posts/create.html')

@bp.route('/posts')
def posts():
    query = sa.select(Post).order_by(Post.created.desc())
    posts = db.session.scalars(query).all()
    return render_template('posts/posts.html', posts=posts)