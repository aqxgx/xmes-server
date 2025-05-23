#!/usr/bin/env python
# -*- coding:utf-8 -*-
<<<<<<< HEAD
# project : xmes_server
=======
# project : xmes-server
>>>>>>> ff50a3cb99533137f0ba3053ad28c0b3f9ab2570
# filename : validators
# author : ly_13
# date : 8/6/2024
import phonenumbers
from django.utils.translation import gettext_lazy as _
from phonenumbers import NumberParseException
from rest_framework import serializers


class PhoneValidator:
    message = _('The phone number format is incorrect')

    def __call__(self, value):
        if not value:
            return

        try:
            phone = phonenumbers.parse(value, 'CN')
            valid = phonenumbers.is_valid_number(phone)
        except NumberParseException:
            valid = False

        if not valid:
            raise serializers.ValidationError(self.message)
