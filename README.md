# Linebot Python Module

## 必要なパッケージをインストール

```
$ git clone https://github.com/JFK/linebot.git
$ pip install -r requirements.txt
```

## importして使う場合

```
import linebot

# 認証の準備
# CHANNEL_***の実装は各自
linebot.CHANNEL_ID = <CHANNEL_ID>
linebot.CHANNEL_SECRET = "<CHANNEL_SECRET>"
linebot.CHANNEL_MID = "<CHANNEL_MID>"

# callback_body
# event_type: 138311609100106403 or 138311609000106303
# to: [from ユーザーID]
# content_type: 1(テキスト) or 2(画像)
# text: ユーザが入力したテキストが入る(content_typeが1の時に設定される)
(event_type, to, content_type, text) = \
    linebot.parse_callback_body(json_data)

# メッセージを送る場合
if content_type == 1:
    msg = u'Linebot使ってるよ！'
    linebot.send_text(to, msg)

# 画像を送る場合
elif content_type == 2:
    content_url = 'http://snapdish.co'
    image_url = u'http://snapdish.co/v3/pc/img/icon_snapdish-512x512.png'
    linebot.send_text([to], content_url, image_url)
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
$ python test_linebot.py <ToのID> <テキストメッセージ>
```
