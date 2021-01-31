# 青空文庫のzipファイルから本文を抽出してテキストデータへ出力

## 青空文庫からデータをDL
[青空文庫](https://www.aozora.gr.jp/index.html)では著作権が消滅した作品や著者が許諾した作品のテキストを公開している．ホームページではそれらの作品を閲覧できるだけではなく，テキストファイルとしてダウンロードすることができる．

　ダウンロード方法は，任意の作品ページを開き，「ファイルをダウンロード」項目から「テキストファイル(ルビなし)」の項目のリンクを取得する．

　次に，スクリプトを実行する際にコマンドにurlをペーストし実行する．

## 実行コマンド
　以下のコマンドを実行することにより，zipファイルをDLすることなく本文のみ(ルビ除く)を抽出したテキストファイルを生成することができる．
```
$ git clone https://github.com/xwasoux/ao2txt.git
$ cd ao2txt/
$ python3 ao2txt.py output.txt https://www.aozora.gr.jp/cards/001518/files/51732_ruby_44617.zip https://www.aozora.gr.jp/cards/001518/files/51731_ruby_50520.zip
```

## 出力結果
　以下の様に出力されれば成功である．
```
zipファイル数:2
- - - - - - - - - - - - - -
抽出中1/2
Download zipfile:  https://www.aozora.gr.jp/cards/001518/files/51732_ruby_44617.zip
zipfile list: ['03gendaigoyaku_kojiki.txt']
- - - - - - - - - - - - - -
抽出中2/2
Download zipfile:  https://www.aozora.gr.jp/cards/001518/files/51731_ruby_50520.zip
zipfile list: ['02kochu_kojiki.txt']
- - - - - - - - - - - - - -
抽出完了!==>../ao2txt/test.txt
```
