#!/usr/bin/env python
# -*- coding: utf-8 -*-

import linebot

if __name__ == '__main__':
    try:
        import sys

        to, msg = (sys.argv[1:])
        print >> sys.stdout, 'Sending...', to, msg

        (code, message) = linebot.send_text([to], unicode(msg, 'utf-8'))
        print >> sys.stdout, 'Sent...', code, message

    except Exception as e:
        print e.message
