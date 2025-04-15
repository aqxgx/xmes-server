#!/usr/bin/env python
# -*- coding:utf-8 -*-
<<<<<<< HEAD
# project : xmes_server
=======
# project : xmes-server
>>>>>>> ff50a3cb99533137f0ba3053ad28c0b3f9ab2570
# filename : expire_config_caches
# author : ly_13
# date : 12/25/2023
from django.core.management.base import BaseCommand

from common.core.config import ConfigCacheBase


class Command(BaseCommand):
    help = 'Expire config caches'

    def add_arguments(self, parser):
        parser.add_argument('key', nargs='?', type=str, default='*')

    def handle(self, *args, **options):
        ConfigCacheBase().invalid_config_cache(options.get('key', '*'))
        ConfigCacheBase(px='user').invalid_config_cache(options.get('key', '*'))
