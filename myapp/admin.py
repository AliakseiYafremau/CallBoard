from django.contrib import admin
from .models import Announcement, Comment

"""Регистрация моделей в админ панели"""
admin.site.register(Announcement)
admin.site.register(Comment)
