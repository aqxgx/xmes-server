#!/usr/bin/env python
# -*- coding:utf-8 -*-
<<<<<<< HEAD
# project : xmes_server
=======
# project : xmes-server
>>>>>>> ff50a3cb99533137f0ba3053ad28c0b3f9ab2570
# filename : alibaba
# author : ly_13
# date : 8/6/2024
import json

from Tea.exceptions import TeaException
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException

from common.utils import get_logger
from .base import BaseSMSClient

logger = get_logger(__name__)


class AlibabaSMS(BaseSMSClient):
    SIGN_AND_TMPL_SETTING_FIELD_PREFIX = 'ALIBABA'

    @classmethod
    def new_from_settings(cls):
        return cls(
            access_key_id=settings.ALIBABA_ACCESS_KEY_ID,
            access_key_secret=settings.ALIBABA_ACCESS_KEY_SECRET
        )

    def __init__(self, access_key_id: str, access_key_secret: str):
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'dysmsapi.aliyuncs.com'
        self.client = Dysmsapi20170525Client(config)

    def send_sms(self, phone_numbers: list, sign_name: str, template_code: str, template_param: dict, **kwargs):
        phone_numbers_str = ','.join(phone_numbers)
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=phone_numbers_str, sign_name=sign_name,
            template_code=template_code, template_param=json.dumps(template_param)
        )
        try:
            logger.info(f'Alibaba sms send: '
                        f'phone_numbers={phone_numbers} '
                        f'sign_name={sign_name} '
                        f'template_code={template_code} '
                        f'template_param={template_param}')
            response = self.client.send_sms(send_sms_request)
            # 这里只判断是否成功，失败抛出异常
            if response.body.code != 'OK':
                raise APIException(detail=response.body.message, code=response.body.code)
        except TeaException as e:
            if e.code == 'SignatureDoesNotMatch':
                raise APIException(code=e.code, detail=_('Signature does not match'))
            raise APIException(code=e.code, detail=e.message)
        return response


client = AlibabaSMS
