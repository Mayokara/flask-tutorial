viewの関数は、アプリケーションへのリクエストへの応答のために書くコード。  

## blueprintの作成  
関連するviewやコードをグループに編成。viewおよびコードをFlaskアプリケーションに登録するのではなく、blueprintに登録する。  
blueprintをFlaskアプリケーションに登録する。  

1. authと名付けられたBlueprintの作成
    - __name__が2番目の引数
    - `__init__.py`のfactory関数にimport

> `__name__`属性: モジュールの名前が格納されている

## 最初のview: Register
2. ユーザがformを提出した場合
    - `request.method`がPOSTになり、入力データの検証を開始。  
    - `request.form`はformのキーと値を対応づける特別なdict。  

3. `username`と`password`が空でないか検証。  

4. usernameが登録済かデータベースに問い合わせ  
    - `db.execute`はプレースホルダ`?`をもつSQLのqueryと、プレースホルダを置き換える値のtupleを受け取る。  
    - `fetchone()`はqueryから1行を返す。  

    > <u>SQL文法 </u>  
    `SELECT`: テーブルに格納されたデータを取得  
    `WHERE`: 取得するデータの条件を設定  

5. 検証成功した場合  
    - 新しいユーザのデータをデータベースにinsert。
    - `generate_password_hash()`を使用してパスワードを安全にハッシュして格納。  
    このqueryはデータを変更するため、変更を保存した後に`db.commit()`を呼び出す必要あり。  
    - ユーザ情報を格納した後、ログインページへリダイレクト。  

6. 検証失敗した場合  
    - エラーをユーザに示す。`flash()`はテンプレート変換(render)するときに取得可能なメッセージを格納。  
    - 登録フォームのあるHTMLを含んだテンプレートの変換。(ユーザが最初に`auth/register`に進んだときも)

> <u>プレースホルダ</u>  
SQLインジェクションを防ぐ。(formに`;DELETE FROM user`を入力される、など)  
入力のパラメータ部分を`?`などで示しておき、実際の値をそこに割り当てる。バインドという。  
与えたい値を`execute()`の第２引数にタプルで渡す。

> <u>ハッシュ化</u>  
パスワードをハッシュ関数を用いてハッシュ値に変換。  
ハッシュ値への変換は計算できるが復元することは困難。(暗号文は鍵があれば複合化できる)  

## ログイン  
7. パスワードの比較  
    - `check_password_hash()`はsubmitされたパスワードを、格納されているハッシュと比較検証。  

8. ユーザのidをsessionに格納  
    - `session`はリクエストを跨いで格納されるデータの`dict`。ユーザの`id`は新しい`session`に格納され、cookieに格納され、ブラウザは以降のリクエストで*cookie*を送信し返す。  

9. 関数の登録とユーザidのsession格納の確認  
    - `bp.before_app_request`はviewの関数実行前に関数を登録する。  
    - `load_logged_in_user`はユーザidが`session`に格納されているかチェックし、取得して`g.user`に格納。
    もし無い場合は`g.user`が`None`になる。  

## ログアウト  
ログアウトするにはユーザidを`session`から取り除く。

## 他のviewでの認証の要求  
ブログの投稿記事を作成、編集、削除するにはログインが必要。  
*decorator*を使用すると、各viewでログインをチェックできる。  

decoratorは適用した元のviewをwrapする新しいviewの関数を返す。  
ユーザ情報が読み込まれてるかチェックして、読み込まれてない場合はログインページへリダイレクトする。  
読み込まれている場合は元のviewが呼び出され通常通りに続ける。

> <u>可変長引数</u>  
関数定義で引数に`*`と`**`をつけると、任意の数の引数(argument)を指定できる。  
`*args`: 複数の引数をtupleとして受け取る。  
`**kwargs`: 複数のキーワード引数をdictとして受け取る。  

## エンドポイントとURL  
Flask実装では、アプリが使用するview用の関数は全て`view_functions`属性に、エンドポイントをキーに関数本体を値にして登録される。  