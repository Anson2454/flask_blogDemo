from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from .auth import login_required
from flaskr import db
from flaskr.models import User, Post

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    query = db.session.query(Post, User)
    posts = query.join(
        User, Post.author_id == User.id).with_entities(
            Post.id, Post.title, Post.body, Post.author_id, Post.created_at,
            User.username
        ).order_by(Post.created_at.desc()).all()

    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        print(g.user)
        if not title:
            error = 'Title is required.'
        if error is not None:
            flash(error)
        else:
            post = Post(title=title, body=body, author_id=session["user_id"])
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    query = db.session.query(Post, User)
    post = query.join(
        User, Post.author_id == User.id
        ).filter(
            Post.id == id
        ).with_entities(
            Post.id, Post.title, Post.body, Post.author_id, Post.created_at,
            User.username
        ).first()
    print(post.author_id)
    print(f"session_id为:{session['user_id']}")
    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post.author_id != session['user_id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            query = db.session.query(Post).filter(Post.id == id)
            query.update({Post.title: title, Post.body: body})
            # new_book = query.first()
            # print(new_book.book_name)
            db.session.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    query = db.session.query(Post)
    query = query.filter(Post.id == id)
    db.session.delete(query.one())
    db.session.commit()
    return redirect(url_for('blog.index'))
