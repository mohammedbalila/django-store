from __future__ import absolute_import, unicode_literals
from celery import task
from .models import CustomUser
from .utils import email_user

# @task(name="email_users")
# def email_users(x, y):
#     users = CustomUser.objects.get()
#     for user in users:
#         email_user(user['email'], '')
 