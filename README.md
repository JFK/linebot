# Linebot Python Module

## 必要なパッケージをインストール

```
$ git clone https://github.com/JFK/linebot.git
$ pip install -r requirements.txt
```

## importして使う場合

```
from linebot import LINEBot
from linebot.const import ContentType

# 認証の準備

# チャンネルIDを設定して、botインスタンスを生成する
bot = LINEBot(<CHANNEL_ID>)

# Credentialの設定をする
bot.CHANNEL_SECRET = "<CHANNEL_SECRET>"
bot.CHANNEL_MID = "<CHANNEL_MID>"

# callbackで受け取った、jsonのデータからreceiveインスタンスを生成する
receive = bot.receive_callback(json_data)

# オペレーションの場合
if receive.is_operation:
    """ 処理を行う """
    """ 登録、削除など """

# メッセージを受信した場合
elif receive.is_message:
    if receive.content('contentType') == ContentType.TEXT:
        to = receive.content('from')
        msg = receive.content('text')
        bot.send_text([to], 'Thanks for your message "%s".' % msg)


# 画像を送る場合
content_url = 'http://snapdish.co'
image_url = u'http://snapdish.co/v3/pc/img/icon_snapdish-512x512.png'
bot.send_image([to], content_url, image_url)
```

## コマンドラインで実行する場合

### 環境を準備

```
$ export LINEBOT_CHANNEL_ID=<CHANNEL_ID>
$ export LINEBOT_CHANNEL_SECRET='<CHANNEL_SECRET>'
$ export LINEBOT_CHANNEL_MID='<CHANNEL_MID>'
```

### テスト実行

```
$ PYTHONPATH=`pwd` python echo.py <CHANNEL_ID> <ToのID> "<テキストメッセージ>"
```
