#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from os import environ

ENDPOINT = 'https://trialbot-api.line.me'

CHANNEL_ID = int(environ.get('LINEBOT_CHANNEL_ID', '<CHANNEL_ID>'))
CHANNEL_SECRET = environ.get('LINEBOT_CHANNEL_SECRET', '<CHANNEL_SECRET>')
CHANNEL_MID = environ.get('LINEBOT_CHANNEL_MID', '<CHANNEL_MID>')


class LineBotError(Exception):
    pass


def build_data(to, content):
    return {
        'to': to,
        'content': content,
        'toChannel': 1383378250,
        'eventType': '138311608800106203'
    }


def content_image(content_url, image_url):
    return {
        'contentType': 2,
        'toType': 1,
        'originalContentUrl': content_url,
        'previewImageUrl': image_url
    }


def content_text(text):
    return {
        'contentType': 1,
        'toType': 1,
        'text': text
    }


def event(to, content):
    headers = {
        'Accept-Language': 'ja-JP,en-US;q=0.7,en-GB;q=0.3',
        'Content-Type': 'application/json; charser=UTF-8',
        'X-Line-ChannelID': CHANNEL_ID,
        'X-Line-ChannelSecret': CHANNEL_SECRET,
        'X-Line-Trusted-User-With-ACL': CHANNEL_MID
    }
    data = requests.post('%s%s' % (ENDPOINT, '/v1/events'),
                         json=build_data(to, content),
                         headers=headers).json()
    response = (data['statusCode'], data['statusMessage'])

    if data['statusCode'] == 200:
        return response

    else:
        raise LineBotError('Error: %s %s' % response)


def send_image(to, content_url, image_url):
    """ イメージを送る """
    content = content_image(content_url, image_url)
    return event(to, content)


def send_text(to, text):
    """ テキストを送る """
    content = content_text(text)
    return event(to, content)


def parse_callback_body(json_body):
    """ json文字列でcallbackのbodyを受け取った場合に使う """
    data = json.loads(json_body)['result'][0]

    _event_type = int(data['eventType'])
    _to = [data['content']['from']]
    _content_type = int(data['content']['contentType'])
    _text = ''

    if _content_type == 1:
        _text = data['content']['text']

    return (_event_type, _to, _content_type, _text)
