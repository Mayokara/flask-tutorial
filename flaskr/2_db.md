## データベース  
- ユーザー情報と投稿記事を格納するためにSQLiteデータベースを使用  
- SQLiteはデータベースサーバを別に用意する必要がない  

## データベースへの接続(connection)
どのような問い合わせ(queries)や操作(operations)にもconnectionが使用され、作業が終了すると閉じられる  
1. 特別なオブジェクト  
    - `g`はリクエストごとに個別。  
    - `current_app`はリクエスト処理中のFlaskアプリケーションを示す。

2. ファイルへのconnectionを確立
    - `sqlite3.connect()`はキー`DATABASE`で示されるファイルへのconnectionを確立する。  
    - `sqlite3.Row`はdictのように振る舞う行を返すようにconnectionheへ伝える。  

3. connectionが作成済みであるか調べる  
    - `close_db`は`g.db`が設定されているか調べることでconnectionが作成済みか調べる。  
    もし存在した場合はそれを閉じる。  

## 表(table)の作成
SQLiteでは、データは表(tables)と列(columns)に格納される。データの格納や取得の前に空の表を作成する必要がある。(`schema.sql`)  
Flaskrではユーザ情報はuser表に、投稿記事はpost表に格納する。  

> <u>テーブルに対する制約</u>  
`PRIMARY KEY`: 主カラムにする  
`AUTOINCREMENT`: データ追加時、格納されたことのある最大値に１を加えた値が自動的に設定される(以前に設定されたことのある値の再使用を防ぐ)  
`UNIQUE`: 重複した値を設定できなくなる  
`NOT NULL`: カラムに格納する値としてNULLを禁止する  
`DEFAULT`: データを追加する際、値を省略した場合のデフォルト値を設定できる  
`FOREIGN KEY`: 外部キー制約。親テーブルと子テーブルの間でデータの整合性を保つ  

> <u>データ型</u>  
`NULL`: NULL値  
`INTEGER`: 符号付き整数  
`TEXT`: テキスト  
`TIMESTAMP`: 日付と時刻の格納に使用するデータ型  

4. schema.sqlのSQLコマンドを実行する関数  
    - `open_resource()`はflaskrから相対的な場所で指定されたファイルを開く。  
    - `click.command()`は`init_db`関数を呼び出して成功時のメッセージを表示するコマンドを定義。  

> 複数のSQL文を１つの呼び出しで実行したい場合、`executescript()`を使用  

## アプリケーションへの登録  
`app.teardown_appcontext()`はレスポンスを返した後のクリーンアップを行っているときに、()内の関数(close_db)を呼び出すようにFlaskに伝える。  
`app.cli.add_command()`は新しいコマンドを追加。  

> `from . import db`: 同じパッケージ(ディレクトリ)から`db.py`をインポート  

## データベースファイルの初期化  
init-dbがappに登録され、flaskコマンドで呼び出せる。  

init-dbコマンドを実行:
```
$ flask init-db
```

> <u>プロトコルとポート</u>  
http | 80番  
https:// | 443番
IPアドレス: 住所  
ドメイン:  IPアドレスを紐付け  
