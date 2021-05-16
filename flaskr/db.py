# データベースへの接続
import sqlite3

import click
# 1. 特別なオブジェクト
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        # 2. ファイルへのconnectionを確立
        g.db = sqlite3.connect(
            current_app.config['DATABASE'], 
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# 3. connectionが作成済みであるか調べる
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# 表(table)の作成
# 4. schema.sqlのSQLコマンドを実行する関数
def init_db():
    db = get_db()
    # 4. 
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database')

# アプリケーションへの登録
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
