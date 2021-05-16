import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# blueprintの作成
# 1. authと名付けられたBlueprintの作成
bp = Blueprint('auth', __name__, url_prefix='/auth')

# 最初のview: Register
@bp.route('/register', methods=('GET', 'POST'))
def register():
    # 2. ユーザがformを提出した場合
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        # 3. usernameとpasswordが空でないか確認
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        # 4. usernameが登録済かデータベースに問い合わせ
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)
        # 5. 検証成功した場合
        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        # 6. 検証失敗した場合
        flash(error)

    return render_template('auth/register.html')

# ログイン
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        
        if user is None:
            error = 'Incorrect username.'
        # 7. パスワードの比較
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        # 8. ユーザのidをsessionに格納
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

            flash(error)

    return render_template('auth/login.html')

# 9. 関数の登録とユーザidのsession格納の確認
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_ids')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

# ログアウト
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# 他のviewでの認証の要求
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
