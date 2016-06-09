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
import sys

if __name__ == '__main__':
    channel_id, to, msg = (sys.argv[1:])
    print >> sys.stdout, 'Sending...', channel_id, to, msg
    bot = LINEBot(channel_id)
    bot.add_text(msg)
    response = bot.send_messages([to])
    print response.data
