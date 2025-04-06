import sqlalchemy as sa

from flask import (
    Blueprint,
    current_app,
    flash,
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
            current_app.logger.info(f"New post by {author}")
            flash(f"Thanks for posting, {author}!", category='success')
            return redirect(url_for('posts.posts'))
        else:
            flash("You need to post a message.", category="error")
        
    return render_template('posts/create.html')

@bp.route('/posts')
def posts():
    query = sa.select(Post).order_by(Post.created.desc())
    posts = db.session.scalars(query).all()
    return render_template('posts/posts.html', posts=posts)

@bp.route('/posts/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    post = db.get_or_404(Post, post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted.', 'success')
    return redirect(url_for('posts.posts'))