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


class Response(object):
    def __init__(self, data):
        self._data = data
        self._is_succeeded = True if isinstance(self.data, dict) and \
            not self.data.get('failed', []) else False

    @property
    def data(self):
        return self._data

    @property
    def is_succeeded(self):
        return self._is_succeeded

    @property
    def http_status(self):
        return self.data.get('httpStatus')

    @property
    def version(self):
        return self.data.get('version')

    @property
    def failed(self):
        return self.data.get('failed')

    @property
    def message_id(self):
        return self.data.get('message_id')

    @property
    def timestamp(self):
        return self.data.get('timestamp')

    @property
    def status_code(self):
        return self.data.get('statusCode')

    @property
    def status_message(self):
        return self.data.get('statusMessage')
