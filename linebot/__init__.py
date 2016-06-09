#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2016 Fumikazu Kiyota
#
# LINE Corporation licenses this file to you under the Apache License,
# version 2.0 (the "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at:
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import requests
from exception import LineBotException
from const import BotAPI
from const import BotAPIChannel
from const import Credential
from const import EventType
from const import RecipientType
from message import MultipleMessageBuilder
from message import MessageBuilder
from response import Response
from receive import Receive


class LINEBot:

    CHANNEL_SECRET = ''
    CHANNEL_MID = ''

    def __init__(self, to_channel, to_type=RecipientType.USER):
        self.multiple_message_builder = MultipleMessageBuilder(to_type=to_type)
        self.to_type = RecipientType.USER
        self.headers = {
            'Accept-Language': 'ja-JP,en-US;q=0.7,en-GB;q=0.3',
            'Content-Type': 'application/json; charser=UTF-8',
            'X-Line-ChannelID': int(to_channel),
            'X-Line-ChannelSecret': self.CHANNEL_SECRET or Credential.CHANNEL_SECRET,
            'X-Line-Trusted-User-With-ACL': self.CHANNEL_MID or Credential.CHANNEL_MID
        }

    def prepare_payload(self, to, content, multi):
        event_type = EventType.SENDING_MULTIPLE_MESSAGES if multi else \
            EventType.SENDING_MESSAGE
        return {
            'to': to,
            'content': content,
            'toChannel': BotAPIChannel.SENDING_CHANNEL_ID,
            'eventType': event_type
        }

    def send_text(self, to, text):
        message = MessageBuilder.text(text, self.to_type)
        return self.send_event(to, message)

    def send_image(self, to, image_url, preview_image_url):
        message = MessageBuilder.image(image_url, preview_image_url,
                                       self.to_type)
        return self.send_event(to, message)

    def send_video(self, to, video_url, preview_image_url):
        message = MessageBuilder.video(video_url, preview_image_url,
                                       self.to_type)
        return self.send_event(to, message)

    def send_audio(self, to, audio_url, duration_millis):
        message = MessageBuilder.audio(audio_url, duration_millis,
                                       self.to_type)
        return self.send_event(to, message)

    def send_location(self, to, text, latitude, longitude):
        message = MessageBuilder.location(text, latitude, longitude,
                                          self.to_type)
        return self.send_event(to, message)

    def send_sticker(self, to, stkid, stkpkgid, stkver=None):
        message = MessageBuilder.sticker(stkid, stkpkgid, stkver, self.to_type)
        return self.send_event(to, message)

    def send_rich_message(self, to, image_url, alt_text, markup):
        message = MessageBuilder.rich_message(image_url, alt_text, markup,
                                              self.to_type)
        return self.send_event(to, message)

    def add_text(self, text):
        self.multiple_message_builder.text(text)

    def add_image(self, image_url, preview_image_url):
        self.multiple_message_builder.image(image_url, preview_image_url)

    def add_video(self, video_url, preview_image_url):
        self.multiple_message_builder.video(video_url, preview_image_url)

    def add_audio(self, audio_url, duration_millis):
        self.multiple_message_builder.audio(audio_url, duration_millis)

    def add_location(self, text, latitude, longitude):
        self.multiple_message_builder.location(text, latitude, longitude)

    def add_sticker(self, stkid, stkpkgid, stkver=None):
        self.multiple_message_builder.add_sticker(stkid, stkpkgid, stkver)

    def add_rich_message(self, image_url, alt_text, markup):
        self.multiple_message_builder.rich_message(image_url, alt_text, markup)

    def send_messages(self, to):
        if self.multiple_message_builder.messages:
            messages = {
                'messageNotified': 0,
                'messages': self.multiple_message_builder.messages
            }
            return self.send_event(to, messages, multi=True)

        else:
            raise LineBotException('multiple_message_builder.messages is empty.')

    def send_event(self, to, message, multi=False):
        data = self.prepare_payload(to, message, multi)
        url = '%s%s' % (BotAPI.SERVER, BotAPI.ENDPOINT_EVENT)
        data = requests.post(url, json=data, headers=self.headers).json()
        response = Response(data)
        if response.is_succeeded:
            return response
        else:
            error_message = (response.status_code, response.status_message)
            raise LineBotException('Error: %s %s' % error_message)

    def receive_callback(self, data):
        return Receive(data)
