## テンプレート  

テンプレートは、静的データと動的データのためのプレースフォルダを含むファイル。  
テンプレート変換にはJinjaが使用される。JinjaではHTMLテンプレートの中で自動変換されるデータの自動エスケープが設定されている。(`<`や`>`のようなHTMLに干渉されかねない文字が入力されても作用しない。)  

Jinjaは静的データとJinja文法を区別するため特別な区切り文字(delimiter)が使われる。  
`{{`と`}}`の間のすべてが最終ドキュメントに出力される式。  
`{%`と`%}`は、`if`や`for`のような制御フロー文を示す。  

@ flaskr/templates/base.html  
`get_flashed_messages()`から返される各メッセージ上をループ

`{% block title %}`: ブラウザのタブおよびウィンドウのタイトルで表示されるタイトル  
`{% block header %}`: ページ上に表示されるタイトル  
`{% block content %}`: ログインformやブログの投稿記事など、各ページのコンテンツ  

## 登録  
@ flaskr/templates/auth/register.html  

`{% extends 'base.html' %}`はベースのテンプレートからブロックを置き換えるものとJinjaに伝える。  
`input`タグは`required`属性を使用。入力欄が記入されないうちはformを提出しないように伝える。

## ログイン  
@ flaskr/templates/auth/login.html  

## ユーザ登録  
上までかけたらユーザ登録が可能。  
ユーザ名とパスワードを記入するとログインページにリダイレクトされる。  

## 静的ファイル  
@ flaskr/static/style.css
CSSに加えてロゴ画像やJavaScriptファイルなども`flaskr_static`ディレクトリ下に置かれ、`url_for('static, filename='...')`で参照される。  