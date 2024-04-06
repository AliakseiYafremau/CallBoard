from django.contrib import admin
from .models import Announcement, Comment, User

"""Регистрация моделей в админ панели"""
admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(User)
