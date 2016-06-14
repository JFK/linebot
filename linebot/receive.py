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
from const import EventType
from const import ContentType


class Receive():
    def __init__(self, data):
        self._index = 0
        self._data = json.loads(data)['result']

    @property
    def total(self):
        return len(self._data)

    @property
    def index(self):
        return self._pointer

    def seek(self, index):
        self._index = index

    def current(self):
        return self._data[self._index]

    def next(self):
        for index, value in enumerate(self._data):
            self._index = index
            yield self.current()

    def content(self, index):
        return self.current()['content'][index]

    @property
    def is_text(self):
        if self.content('contentType') == ContentType.TEXT:
            return True

    @property
    def is_image(self):
        if self.content('contentType') == ContentType.IMAGE:
            return True

    @property
    def is_video(self):
        if self.content('contentType') == ContentType.VIDEO:
            return True

    @property
    def is_audio(self):
        if self.content('contentType') == ContentType.AUDIO:
            return True

    @property
    def is_location(self):
        if self.content('contentType') == ContentType.LOCATION:
            return True

    @property
    def is_sticker(self):
        if self.content('contentType') == ContentType.STICKER:
            return True

    @property
    def is_rich_message(self):
        if self.content('contentType') == ContentType.RICH_MESSAGE:
            return True

    @property
    def is_message(self):
        if self.current()['eventType'] == EventType.RECEIVING_MESSAGE:
            return True

    @property
    def is_operation(self):
        if self.current()['eventType'] == EventType.RECEIVING_OPERATION:
            return True
