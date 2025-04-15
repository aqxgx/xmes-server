#!/usr/bin/env python
# -*- coding:utf-8 -*-
<<<<<<< HEAD
# project : xmes_server
=======
# project : xmes-server
>>>>>>> ff50a3cb99533137f0ba3053ad28c0b3f9ab2570
# filename : local
# author : ly_13
# date : 10/18/2024


from asgiref.local import Local

thread_local = Local(thread_critical=True)


def _find(attr):
    return getattr(thread_local, attr, None)
