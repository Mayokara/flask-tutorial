## 青写真  
- `blog.py`でblueprintを定義  
- `__init__.py`で`app.register_blueprint()`を使って登録する。  

@`__init__.py`  
authのblueprintとは異なりblogのblueprintは`url_prefix`を持たない。  
→今回はブログのindexをメインのindexにしている。  
`index`のviewの場所は`/`になり、`create`のviewの場所は`/create`になる。  

しかし定義上は`blog.index`  
`index`と`blog.index`どちらも同一の`/`をURLとして生成するように`app.add_url_rule()`はエンドポイント名`'index'`をURLの`/`を関連づける  

## Index  
@ flaskr/blog.py
1. 投稿記事の表示  
    - userテーブルから作者情報使用のために`JOIN`を使用  

> <u>SQL文法 </u>  
> - テーブル結合   
`INNER JOIN`: 指定したテーブルのカラム値が一致するデータのみ取得、INNERは省略されることも。    
`OUTER JOIN`: カラム値が一致するデータだけでなくどちらかのテーブルだけにある場合も合わせて取得する  
`CROSS JOIN`: ２つのテーブルのデータの全ての組み合わせを取得する  
`SELECT (取得するカラム) FROM テーブル名1 INNER JOIN テーブル名2 ON (結合条件);`  
> - データの取得  
`ORDER BY`: 取得したデータをカラムの値でソート。`ASC`: 昇順、`DESC`: 降順  

## Create  
authの`register`のviewと同じように機能。  

> <u>SQL文法 </u>   
`INSERT`: テーブルにデータを追加。  
`INSERT INTO テーブル名 VALUES(値1, 値2, ...);`  

## Update  
`update`と`delete`のviewは両方とも、`id`を使って`post`を取得し、ログインユーザと作者が一致しているか検証する。  

2. チェックとエラー表示
    - `abort()`はHTTPのステータスコードを返す特殊な例外を発生させる。  
    `404`: Not Found  
    `403`: Forbidden  Found
    `401`: Unauthorized  

    - `check_author`引数を定義するのは、作者をチェックせずに`post`を取得するときにこの関数を使用可能にするため。  

3. updateのview  
    - `update`関数は`id`引数を受け取る(`<int:id>`部分に対応)。  

> <u>SQL文法 </u>  
`UPDATE`: データの更新  

## Delete  
