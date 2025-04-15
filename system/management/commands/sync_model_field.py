#!/usr/bin/env python
# -*- coding:utf-8 -*-
<<<<<<< HEAD
# project : xmes_server
=======
# project : xmes-server
>>>>>>> ff50a3cb99533137f0ba3053ad28c0b3f9ab2570
# filename : sync_model_field
# author : ly_13
# date : 10/25/2024
from django.core.management.base import BaseCommand

from system.utils.modelfield import sync_model_field


class Command(BaseCommand):
    help = 'Sync Model Field'

    def handle(self, *args, **options):
        sync_model_field()
