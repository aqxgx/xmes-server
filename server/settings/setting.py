#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project : xmes-server
# filename : setting
# author : ly_13
# date : 10/18/2024
import os

from ..const import PROJECT_DIR, CONFIG

# 密码安全配置
SECURITY_PASSWORD_MIN_LENGTH = CONFIG.SECURITY_PASSWORD_MIN_LENGTH
SECURITY_ADMIN_USER_PASSWORD_MIN_LENGTH = CONFIG.SECURITY_ADMIN_USER_PASSWORD_MIN_LENGTH
SECURITY_PASSWORD_UPPER_CASE = CONFIG.SECURITY_PASSWORD_UPPER_CASE
SECURITY_PASSWORD_LOWER_CASE = CONFIG.SECURITY_PASSWORD_LOWER_CASE
SECURITY_PASSWORD_NUMBER = CONFIG.SECURITY_PASSWORD_NUMBER
SECURITY_PASSWORD_SPECIAL_CHAR = CONFIG.SECURITY_PASSWORD_SPECIAL_CHAR
SECURITY_PASSWORD_RULES = [
    'SECURITY_PASSWORD_MIN_LENGTH',
    'SECURITY_PASSWORD_UPPER_CASE',
    'SECURITY_PASSWORD_LOWER_CASE',
    'SECURITY_PASSWORD_NUMBER',
    'SECURITY_PASSWORD_SPECIAL_CHAR'
]

# 用户登录限制的规则
SECURITY_LOGIN_LIMIT_COUNT = CONFIG.SECURITY_LOGIN_LIMIT_COUNT
SECURITY_LOGIN_LIMIT_TIME = CONFIG.SECURITY_LOGIN_LIMIT_TIME  # Unit: minute
SECURITY_CHECK_DIFFERENT_CITY_LOGIN = CONFIG.SECURITY_CHECK_DIFFERENT_CITY_LOGIN
# 登录IP限制的规则
SECURITY_LOGIN_IP_BLACK_LIST = CONFIG.SECURITY_LOGIN_IP_BLACK_LIST
SECURITY_LOGIN_IP_WHITE_LIST = CONFIG.SECURITY_LOGIN_IP_WHITE_LIST
SECURITY_LOGIN_IP_LIMIT_COUNT = CONFIG.SECURITY_LOGIN_IP_LIMIT_COUNT
SECURITY_LOGIN_IP_LIMIT_TIME = CONFIG.SECURITY_LOGIN_IP_LIMIT_TIME

# 登陆规则
SECURITY_LOGIN_ACCESS_ENABLED = CONFIG.SECURITY_LOGIN_ACCESS_ENABLED
SECURITY_LOGIN_CAPTCHA_ENABLED = CONFIG.SECURITY_LOGIN_CAPTCHA_ENABLED
SECURITY_LOGIN_ENCRYPTED_ENABLED = CONFIG.SECURITY_LOGIN_ENCRYPTED_ENABLED
SECURITY_LOGIN_TEMP_TOKEN_ENABLED = CONFIG.SECURITY_LOGIN_TEMP_TOKEN_ENABLED
SECURITY_LOGIN_BY_EMAIL_ENABLED = CONFIG.SECURITY_LOGIN_BY_EMAIL_ENABLED
SECURITY_LOGIN_BY_SMS_ENABLED = CONFIG.SECURITY_LOGIN_BY_SMS_ENABLED
SECURITY_LOGIN_BY_BASIC_ENABLED = CONFIG.SECURITY_LOGIN_BY_BASIC_ENABLED

# 注册规则
SECURITY_REGISTER_ACCESS_ENABLED = CONFIG.SECURITY_REGISTER_ACCESS_ENABLED
SECURITY_REGISTER_CAPTCHA_ENABLED = CONFIG.SECURITY_REGISTER_CAPTCHA_ENABLED
SECURITY_REGISTER_ENCRYPTED_ENABLED = CONFIG.SECURITY_REGISTER_ENCRYPTED_ENABLED
SECURITY_REGISTER_TEMP_TOKEN_ENABLED = CONFIG.SECURITY_REGISTER_TEMP_TOKEN_ENABLED
SECURITY_REGISTER_BY_EMAIL_ENABLED = CONFIG.SECURITY_REGISTER_BY_EMAIL_ENABLED
SECURITY_REGISTER_BY_SMS_ENABLED = CONFIG.SECURITY_REGISTER_BY_SMS_ENABLED
SECURITY_REGISTER_BY_BASIC_ENABLED = CONFIG.SECURITY_REGISTER_BY_BASIC_ENABLED
# 忘记密码规则
SECURITY_RESET_PASSWORD_ACCESS_ENABLED = CONFIG.SECURITY_RESET_PASSWORD_ACCESS_ENABLED
SECURITY_RESET_PASSWORD_CAPTCHA_ENABLED = CONFIG.SECURITY_RESET_PASSWORD_CAPTCHA_ENABLED
SECURITY_RESET_PASSWORD_TEMP_TOKEN_ENABLED = CONFIG.SECURITY_RESET_PASSWORD_TEMP_TOKEN_ENABLED
SECURITY_RESET_PASSWORD_ENCRYPTED_ENABLED = CONFIG.SECURITY_RESET_PASSWORD_ENCRYPTED_ENABLED
SECURITY_RESET_PASSWORD_BY_EMAIL_ENABLED = CONFIG.SECURITY_RESET_PASSWORD_BY_EMAIL_ENABLED
SECURITY_RESET_PASSWORD_BY_SMS_ENABLED = CONFIG.SECURITY_RESET_PASSWORD_BY_SMS_ENABLED

# 绑定邮箱
SECURITY_BIND_EMAIL_ACCESS_ENABLED = CONFIG.SECURITY_BIND_EMAIL_ACCESS_ENABLED
SECURITY_BIND_EMAIL_CAPTCHA_ENABLED = CONFIG.SECURITY_BIND_EMAIL_CAPTCHA_ENABLED
SECURITY_BIND_EMAIL_TEMP_TOKEN_ENABLED = CONFIG.SECURITY_BIND_EMAIL_TEMP_TOKEN_ENABLED
SECURITY_BIND_EMAIL_ENCRYPTED_ENABLED = CONFIG.SECURITY_BIND_EMAIL_ENCRYPTED_ENABLED

# 绑定手机
SECURITY_BIND_PHONE_ACCESS_ENABLED = CONFIG.SECURITY_BIND_PHONE_ACCESS_ENABLED
SECURITY_BIND_PHONE_CAPTCHA_ENABLED = CONFIG.SECURITY_BIND_PHONE_CAPTCHA_ENABLED
SECURITY_BIND_PHONE_TEMP_TOKEN_ENABLED = CONFIG.SECURITY_BIND_PHONE_TEMP_TOKEN_ENABLED
SECURITY_BIND_PHONE_ENCRYPTED_ENABLED = CONFIG.SECURITY_BIND_PHONE_ENCRYPTED_ENABLED

# 基本配置
SITE_URL = CONFIG.SITE_URL
FRONT_END_WEB_WATERMARK_ENABLED = CONFIG.FRONT_END_WEB_WATERMARK_ENABLED  # 前端水印展示
PERMISSION_FIELD_ENABLED = CONFIG.PERMISSION_FIELD_ENABLED  # 字段权限控制
PERMISSION_DATA_ENABLED = CONFIG.PERMISSION_DATA_ENABLED  # 数据权限控制
REFERER_CHECK_ENABLED = CONFIG.REFERER_CHECK_ENABLED  # referer 校验
EXPORT_MAX_LIMIT = CONFIG.EXPORT_MAX_LIMIT  # 限制导出数据数量

# 验证码配置
VERIFY_CODE_TTL = CONFIG.VERIFY_CODE_TTL  # Unit: second
VERIFY_CODE_LIMIT = CONFIG.VERIFY_CODE_LIMIT
VERIFY_CODE_LENGTH = CONFIG.VERIFY_CODE_LENGTH
VERIFY_CODE_LOWER_CASE = CONFIG.VERIFY_CODE_LOWER_CASE
VERIFY_CODE_UPPER_CASE = CONFIG.VERIFY_CODE_UPPER_CASE
VERIFY_CODE_DIGIT_CASE = CONFIG.VERIFY_CODE_DIGIT_CASE

# 邮件配置
EMAIL_ENABLED = CONFIG.EMAIL_ENABLED
EMAIL_HOST = CONFIG.EMAIL_HOST
EMAIL_PORT = CONFIG.EMAIL_PORT
EMAIL_HOST_USER = CONFIG.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = CONFIG.EMAIL_HOST_PASSWORD
EMAIL_FROM = CONFIG.EMAIL_FROM
EMAIL_RECIPIENT = CONFIG.EMAIL_RECIPIENT
EMAIL_SUBJECT_PREFIX = CONFIG.EMAIL_SUBJECT_PREFIX
EMAIL_USE_SSL = CONFIG.EMAIL_USE_SSL
EMAIL_USE_TLS = CONFIG.EMAIL_USE_TLS

# 短信配置
SMS_ENABLED = CONFIG.SMS_ENABLED
SMS_BACKEND = CONFIG.SMS_BACKEND
SMS_TEST_PHONE = CONFIG.SMS_TEST_PHONE

# 阿里云短信配置
ALIBABA_ACCESS_KEY_ID = CONFIG.ALIBABA_ACCESS_KEY_ID
ALIBABA_ACCESS_KEY_SECRET = CONFIG.ALIBABA_ACCESS_KEY_SECRET
ALIBABA_VERIFY_SIGN_NAME = CONFIG.ALIBABA_VERIFY_SIGN_NAME
ALIBABA_VERIFY_TEMPLATE_CODE = CONFIG.ALIBABA_VERIFY_TEMPLATE_CODE

# 图片验证码
CAPTCHA_IMAGE_SIZE = CONFIG.CAPTCHA_IMAGE_SIZE  # 设置 captcha 图片大小
CAPTCHA_CHALLENGE_FUNCT = CONFIG.CAPTCHA_CHALLENGE_FUNCT
CAPTCHA_LENGTH = CONFIG.CAPTCHA_LENGTH  # 字符个数,仅针对随机字符串生效
CAPTCHA_TIMEOUT = CONFIG.CAPTCHA_TIMEOUT  # 超时(minutes)
CAPTCHA_FONT_SIZE = CONFIG.CAPTCHA_FONT_SIZE
CAPTCHA_BACKGROUND_COLOR = CONFIG.CAPTCHA_BACKGROUND_COLOR
CAPTCHA_FOREGROUND_COLOR = CONFIG.CAPTCHA_FOREGROUND_COLOR
CAPTCHA_NOISE_FUNCTIONS = CONFIG.CAPTCHA_NOISE_FUNCTIONS

# 下面图片验证码 默认配置
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
# CAPTCHA_NOISE_FUNCTIONS = ("captcha.helpers.noise_arcs", "captcha.helpers.noise_dots")
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_FONT_PATH = os.path.join(PROJECT_DIR, "captcha", "fonts", "Vera.ttf")
CAPTCHA_LETTER_ROTATION = (-35, 35)
CAPTCHA_FILTER_FUNCTIONS = ("captcha.helpers.post_smooth",)
CAPTCHA_PUNCTUATION = """_"',.;:-"""
CAPTCHA_FLITE_PATH = None
CAPTCHA_SOX_PATH = None
CAPTCHA_MATH_CHALLENGE_OPERATOR = "*"
CAPTCHA_GET_FROM_POOL = False
CAPTCHA_GET_FROM_POOL_TIMEOUT = 5
CAPTCHA_2X_IMAGE = True
