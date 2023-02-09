# workspace
Djangoのお試しrepository

# 開発環境
- VS Code + Remote-Containers拡張機能
- Docker Desktop v4.16.3 + WSL2 / win11
 
# 環境構成
dev container上にMySQL, PHP,  Djangoの3つのコンテナを展開。  
コンテナの構成は[docker-compose.yml](https://github.com/s-taira/workspace/blob/main/.devcontainer/docker-compose.yml)参照

DJangoの環境は[DockerFile](https://github.com/s-taira/workspace/blob/main/.devcontainer/Dockerfile)参照

# アプリケーション構成
testApiApp -> プロジェクト
images -> APIアプリ

APIはRestFrameworkを利用。  
API Viewはview.pyではなくapi.pyを用意しそちらに記述。  

# 実行手順
codeをpull後、VisualStdio Codeより"Open Folder in Contaier"を実行するとコンテナが作成されます。  
  
マイグレーション機能を利用してtableを作成します。  
```# python manage.py makemigrations```  
```# python manage.py migrate```

# その他
POSTリクエストを処理するAPIを用意しています。(api/images)  
その処理の中であるサイトにjsonでresponseが帰ってくる想定でAPIリクエストを投げますが、サイト情報が返ってくるため動作しません。  
test.pyのほうにモックを使ったテストを記載しているので動作確認はこちらにて。  
```# python manage.py test```  

なお、UIは用意しておらずAPIのみの実装になっています。  

Djangoは初経験、pythonはちょっとしたスクリプトを書く程度なのでコードは参考程度でお願いします。



