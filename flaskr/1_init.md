## アプリケーションファクトリー  
Flaskインスタンスをグローバルで作成する代わりに、関数の内側で作成するようにする。  

`create_app`はapplication factoryの関数  

1. Flaskインスタンスを生成  
    - `__name__`はPythonのmodule名  
    - `instance_relative_config=True`は設定ファイル(の場所)がインスタンスフォルダから相対的に示されることをappに伝える。  

2. appが使用する標準設定をいくつか設定
    - `SECRET KEY`はデータを安全に保つためにFlaskが使用。  
    - `DATABASE`はSQLiteデータベースファイルが保存されるパス。`app.instance_path`の下。  

3. 標準設定の上書き  
    - もしインスタンスフォルダに`config.py`があれば標準設定を上書き。  
    - `test_config`もfactoryに渡すことも可能  

4. インスタンスフォルダの存在を確実にする  
    - `os.makedirs()`は`app.instance_path`が確実に存在するようにする。

5. アプリケーションが機能してるか確認するための簡易なrouteを作成  
    - URLの`/hello`と`'Hello, World!'`というレスポンスを返す関数を結びつける。  

## 仮想環境の用意
```
. venv/bin/activate
```

## アプリケーションの実行
```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```