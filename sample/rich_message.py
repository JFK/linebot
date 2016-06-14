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


from linebot import LINEBot
from linebot.message import RichMessageBuilder
import sys

if __name__ == '__main__':
    channel_id, to = (sys.argv[1:])
    print >> sys.stdout, 'Sending...', channel_id, to
    bot = LINEBot(channel_id)
    rich_message = RichMessageBuilder()
    rich_message.add_message(action_name='getApp',
                             text='乾杯ビール',
                             link_url='http://snapdish.co/d/T8zS8a',
                             x=0, y=0,
                             width=1040,
                             height=1040)
    image_url = 'http://d9126knutfuyw.cloudfront.net/photo/dish/%s/crop'
    image_url = image_url % '5759637d0acd0b6bf63da607'
    alt_text = '料理写真の詳細ページもご覧ください'
    bot.add_rich_message(image_url, alt_text, rich_message.build())
    response = bot.send_messages([to])
    print response.data
