from flask import (
    Blueprint, 
    render_template, 
    redirect, 
    request, 
    url_for,
)
from board.extensions import db


bp = Blueprint('posts', __name__)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        author = request.form['author'] or 'Anonymous'
        message = request.form['message']

        if message:
            pass
    return render_template('posts/create.html')

@bp.route('/posts')
def posts():
    posts = []
    return render_template('posts/posts.html', posts=posts)