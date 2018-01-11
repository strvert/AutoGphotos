# AutoGphotos
Google Photosの前身であるPicasaのAPIが生存していることを利用して利便性の高いGoogle Photosアップロードツールを作成しようとしていましたが、Picasa時代の制限により480x360以上の動画ファイルがこのAPIではアップロード不可能なことが発覚したため開発を中断しました。  
画像に対しては特に制限なく利用できるので、管理機能は実装していませんがコマンドでGoogle Photosに画像をアップロードできるツールとしては利用可能です。

# 完成してないけど使える範囲の使い方
https://console.developers.google.com/apis/credentials  
で、GooglePhotosのバックアップ先アカウントを用いてプロジェクトを作成し、client idとsecret idを取得する。  

setup.pyを実行し、指示に従ってセットアップを行う。  
セットアップ完了のメッセージが出たらアカウントの登録は完了している。  
  
uptest.pyを、``python uptest.py [画像ファイル]``の型式で実行すればGoogle Photosに画像が上がっているはずです。上手いことシェルスクリプトとかで実行制御してcronでも連携させればLinux版のアップローダとして使える。  

僕は動画をアップロードしたくて作ってたの……。

## うごく
