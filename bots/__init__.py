# -*- coding:utf-8 -*-
"""
# @PROJECT: automatic_update
# @Author: admin
# @Date:   2019-04-02 14:49:37
# @Last Modified by:   admin
# @Last Modified time: 2019-04-02 14:49:37
"""
def setup_django_env():
    import os, django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "automatic_update.settings")
    django.setup()

def check_db_connection():
    from django.db import connection

    if connection.connection:
        #NOTE: (zacky, 2016.MAR.21st) IF CONNECTION IS CLOSED BY BACKEND, CLOSE IT AT DJANGO, WHICH WILL BE SETUP AFTERWARDS.
        if not connection.is_usable():
            connection.close()