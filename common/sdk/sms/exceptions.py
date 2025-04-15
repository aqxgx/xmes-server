#!/usr/bin/env python
# -*- coding:utf-8 -*-
<<<<<<< HEAD
# project : xmes_server
=======
# project : xmes-server
>>>>>>> ff50a3cb99533137f0ba3053ad28c0b3f9ab2570
# filename : exceptions
# author : ly_13
# date : 8/6/2024

from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException


class CodeExpired(APIException):
    default_code = 'verify_code_expired'
    default_detail = _('The verification code has expired. Please resend it')


class CodeError(APIException):
    default_code = 'verify_code_error'
    default_detail = _('The verification code is incorrect')


class CodeSendTooFrequently(APIException):
    default_code = 'code_send_too_frequently'
    default_detail = _('Please wait {} seconds before sending')

    def __init__(self, ttl):
        super().__init__(detail=self.default_detail.format(ttl))


class CodeSendOverRate(APIException):
    default_code = 'code_send_over_rate'
    default_detail = _('Please wait {} seconds before sending')

    def __init__(self, ttl):
        super().__init__(detail=self.default_detail.format(ttl))
