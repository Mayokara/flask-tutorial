ユニットテストを書くことでコードが動くかチェック  
`pytest`と`coverage`を使用  

## 準備と据付品  

テスト用コードはtestsディレクトリに置く。
- `conftest.py`は各テストで使用していく据付品(fixtures)と呼ばれる準備用(setup)関数を含む  
- 各テストで新しく一時的なデータベースを作成する。(`data.sql`)  

1. a  
    - `tempfile.mkstemo()`: 一時ファイルを作成して開き、fileオブジェクトとパスを返す。  
    - `TESTING`: appがテストモードであることをFlaskに伝える。  

2. clientを使用して、サーバを実行させずにアプリケーションへのリクエストを作成  
    - fixtureは、`app.test_client()`を呼び出す。
    - runner関数のfixtureは


> デコレータ: 引数にとった関数の引数を使いたい  
