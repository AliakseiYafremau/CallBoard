from django import forms
from allauth.account.forms import SignupForm

from string import hexdigits
from random import sample

from django.core.mail import send_mail
from django.forms import TextInput

from callboard import settings
from .models import Announcement, Comment


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class AnnouncementCreateForm(forms.ModelForm):
    """Форма создания объявления"""
    file = MultipleFileField(label='Select files', required=False)
    class Meta:
        model = Announcement
        fields = ['title', 'text', 'category']


class CommentForm(forms.ModelForm):
    """Форма создания комментария"""

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        initial['text'] = ''
        kwargs['initial'] = initial
        super(CommentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={'placeholder': 'Enter your comment'})
        }


class CustomSignUpForm(SignupForm):
    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.is_active = False
        code = ''.join(sample(hexdigits, 5))
        user.code = code
        user.save()
        send_mail(
            subject=f'Code of activation',
            message=f'Code of activation: {user.code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return user
