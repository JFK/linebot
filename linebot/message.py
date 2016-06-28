#!/usr/bin/env python

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


import json
from const import ContentType
from const import RecipientType
USER = RecipientType.USER


class MessageBuilder(object):
    @classmethod
    def text(self, text, to_type=USER):
        return {
            'contentType': ContentType.TEXT,
            'toType': to_type,
            'text': text
        }

    @classmethod
    def image(self, image_url, preview_image_url, to_type=USER):
        return {
            'contentType': ContentType.IMAGE,
            'toType': to_type,
            'originalContentUrl': image_url,
            'previewImageUrl': preview_image_url
        }

    @classmethod
    def video(self, video_url, preview_image_url, to_type=USER):
        return {
            'contentType': ContentType.VIDEO,
            'toType': to_type,
            'originalContentUrl': video_url,
            'previewImageUrl': preview_image_url
        }

    @classmethod
    def audio(self, audio_url, duration_millis, to_type=USER):
        return {
            'contentType': ContentType.AUDIO,
            'toType': to_type,
            'originalContentUrl': audio_url,
            'contentMetadata': {
                'AUDLEN': '%s' % duration_millis
            }
        }

    @classmethod
    def location(self, text, latitude, longitude, to_type=USER):
        return {
            'contentType': ContentType.LOCATION,
            'toType': to_type,
            'text': text,
            'location': {
                'title': text,
                'latitude': latitude,
                'longitude': longitude,
            }
        }

    @classmethod
    def sticker(self, stkid, stkpkgid, stkver=None,
                to_type=USER):
        meta = {
            'STKID': '%s' % stkid,
            'STKPKGID': '%s' % stkpkgid
        }
        if stkver is not None:
            meta.update({'STKVER': '%s' % stkver})

        return {
            'contentType': ContentType.STICKER,
            'toType': to_type,
            'contentMetadata': meta,
        }

    @classmethod
    def rich_message(self, image_url, alt_text, markup,
                     to_type=USER):
        return {
            'contentType': ContentType.RICH_MESSAGE,
            'toType': to_type,
            'contentMetadata': {
                'SPEC_REV': '1',
                'DOWNLOAD_URL': image_url,
                'ALT_TEXT': alt_text,
                'MARKUP_JSON': markup
            }
        }


class RichMessageBuilder(object):
    def __init__(self):
        self.actions = {}
        self.listeners = []

    def add_message(self, **attrs):
        self.set_action(attrs['action_name'], attrs['text'],
                        attrs['link_url'])
        self.add_listener(attrs['action_name'], attrs['x'], attrs['y'],
                          attrs['width'], attrs['height'])

    def add_listener(self, action_name, x, y, width, height):
        if not (isinstance(action_name, str) and
                isinstance(x, int) and
                isinstance(y, int) and
                isinstance(width, int) and
                isinstance(height, int)):
            raise ValueError('Invalid value type.')

        if action_name not in self.actions:
            raise ValueError('action_name is not found in self.actions.')

        self.listeners.append({
            'type': 'touch',  # Fixed value
            'params': [x, y, width, height],
            'action': action_name
        })

    def set_action(self, action_name, text, link_url, action_type='web'):
        self.actions.update({
            action_name: {
                'type': action_type,
                'text': str(text),
                'params': {'linkUri': str(link_url)}
            }
        })

    def calc_height(self):
        height = 0
        for x in self.listeners:
            h = x['params'][1] + x['params'][3]  # y + height
            if height < h:
                height = h
        return 2080 if height > 2080 else height

    def build(self):
        width = 1040  # Fixed value
        height = self.calc_height()
        scene_name = 'scene1'  # Fixed value
        image_name = 'image1'  # Fixed value
        x = 0  # Fixed value
        y = 0  # Fixed value
        return json.dumps({
            'canvas': {
                'width': width,
                'height': height,
                'initialScene': scene_name
            },
            'images': {
                image_name: {
                    'x': x,
                    'y': y,
                    'w': width,
                    'h': height
                }
            },
            'actions': self.actions,
            'scenes': {
                scene_name: {
                    'draws': [{
                        'image': image_name,
                        'x': x,
                        'y': y,
                        'w': width,
                        'h': height
                    }],
                    'listeners': self.listeners,
                }
            }
        })


class MultipleMessageBuilder(object):
    def __init__(self, to_type=USER):
        self.messages = []
        self.to_type = to_type

    def text(self, text):
        message = MessageBuilder.text(text, self.to_type)
        self.messages.append(message)

    def image(self, image_url, preview_image_url):
        message = MessageBuilder.image(image_url, preview_image_url,
                                       self.to_type)
        self.messages.append(message)

    def video(self, video_url, preview_image_url):
        message = MessageBuilder.video(video_url, preview_image_url,
                                       self.to_type)
        self.messages.append(message)

    def audio(self, audio_url, duration_millis):
        message = MessageBuilder.audio(audio_url, duration_millis,
                                       self.to_type)
        self.messages.append(message)

    def location(self, text, latitude, longitude):
        message = MessageBuilder.location(text, latitude, longitude,
                                          self.to_type)
        self.messages.append(message)

    def sticker(self, stkid, stkpkgid, stkver=None):
        message = MessageBuilder.sticker(stkid, stkpkgid, stkver, self.to_type)
        self.messages.append(message)

    def rich_message(self, image_url, alt_text, markup):
        message = MessageBuilder.rich_message(image_url, alt_text, markup,
                                              self.to_type)
        self.messages.append(message)
