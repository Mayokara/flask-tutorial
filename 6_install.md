プロジェクトの依存対象を他のパッケージと同じようなやり方で管理可能。  
`pip install yourproject.whl`で依存対象をインストール可能。  

## プロジェクトの記述  
- `packages`はどのpackageディレクトリを含めるべきかPythonに伝える。  
- `find_packages()`はディレクトリを自動的に見つけ出す。  
- Pythonのpackageではないその他のファイルを含めるには`include_package_data`を設定する。  
- その他のデータが何かを伝えるには`MANIFEST.in`ファイルが必要。  

## プロジェクトのインストール  
`pip`を使って自分のプロジェクトを仮想環境へインストール (`-e`: editableまたはdevelopmentモードでインストール)  
```
$ pip install -e .
```

プロジェクトの確認  
```
$ pip list
```
