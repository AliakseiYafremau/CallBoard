from django import forms

from .models import Announcement, Comment


class AnnouncementCreateForm(forms.ModelForm):
    """Форма создания объявления"""
    class Meta:
        model = Announcement
        fields = ['title', 'text', 'category']


class CommentForm(forms.ModelForm):
    """Форма создания комментария"""
    class Meta:
        model = Comment
        fields = ['text']
