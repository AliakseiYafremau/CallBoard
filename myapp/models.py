from django.shortcuts import reverse
from django.contrib.auth.models import User, AbstractUser
from django.db import models

from .categories import CATEGORIES


class User(AbstractUser):
    code = models.CharField(max_length=15, blank=True, null=True)


class Announcement(models.Model):
    """Класс объявления"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    text = models.TextField()
    category = models.CharField(max_length=255, choices=CATEGORIES, default="Прочее")
    date_of_creation = models.DateTimeField(auto_now_add=True)

    # Путь к этой модели на сайте
    def get_absolute_url(self):
        return reverse('announce_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Класс отклика"""
    # При удалении пользователя сам комментарий(отклик) остается
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # При удалении объявления все комментарии удаляются
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    data_of_creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('announce_detail', args=[str(self.announcement_id)])

    def __str__(self):
        return f"{self.announcement}|{self.user}|{self.text[:10]}"


