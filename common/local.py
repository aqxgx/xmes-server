#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project : xmes_server
# filename : local
# author : ly_13
# date : 10/18/2024


from asgiref.local import Local

thread_local = Local(thread_critical=True)


def _find(attr):
    return getattr(thread_local, attr, None)
