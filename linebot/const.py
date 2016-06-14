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

from os import environ


class BotAPI:
    SERVER = 'https://trialbot-api.line.me'
    ENDPOINT_EVENT = '/v1/events'
    ENDPOINT_BOT = '/v1/bot'


class Credential:
    CHANNEL_SECRET = environ.get('LINEBOT_CHANNEL_SECRET', '<CHANNEL_SECRET>')
    CHANNEL_MID = environ.get('LINEBOT_CHANNEL_MID', '<CHANNEL_MID>')


class BotAPIChannel:
    RECEIVING_CHANNEL_ID = 1341301815
    RECEIVING_CHANNEL_MID = 'u206d25c2ea6bd87c17655609a1c37cb8'
    SENDING_CHANNEL_ID = 1383378250


class ContentType:
    TEXT = 1
    IMAGE = 2
    VIDEO = 3
    AUDIO = 4
    LOCATION = 7
    STICKER = 8
    CONTACT = 10
    RICH_MESSAGE = 12


class EventType:
    RECEIVING_MESSAGE = '138311609000106303'
    RECEIVING_OPERATION = '138311609100106403'
    SENDING_MESSAGE = '138311608800106203'
    SENDING_MULTIPLE_MESSAGES = '140177271400161403'


class OperationType:
    ADDED_AS_FRIEND = 4
    BLOCKED = 8


class RecipientType:
    USER = 1
