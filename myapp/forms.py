from django import forms

from .models import Announcement


class AnnouncementCreateForm(forms.ModelForm):
    """Форма создания объявления"""
    class Meta:
        model = Announcement
        fields = ['title', 'text', 'category']
