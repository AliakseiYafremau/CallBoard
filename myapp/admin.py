from django.contrib import admin
from .models import Announcement, Comment, User, AnnouncementContent, Content

"""Регистрация моделей в админ панели"""
admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Content)
admin.site.register(AnnouncementContent)
