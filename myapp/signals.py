from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from callboard import settings
from myapp.models import Comment


@receiver(post_save, sender=Comment)
def notify_about_new_comment(sender, instance, **kwargs):
    """ Сигнал фиксирующий создании/изменении отклика """
    # FIXME письмо отправляется два раза
    user_received = instance.announcement.user
    commentator = instance.user
    content = render_to_string(
        'receiving_comment.html',
        {
            'user_received': user_received.username,
            'user_sent': commentator,
            'text': instance.text,
        }
    )

    msg = EmailMultiAlternatives(
        subject='New comment',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user_received.email],
    )

    msg.attach_alternative(content, 'text/html')
    msg.send()
