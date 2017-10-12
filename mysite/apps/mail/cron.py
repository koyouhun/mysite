from django.core import mail as dj_mail
from django.conf import settings

from mysite.templates.email.template import player_regist_template
from .models import Mail


def email_sending():
    for mail in Mail.objects.all():
        dj_mail.send_mail(
            subject='[할로윈 파티] 신청 확인',
            message=player_regist_template,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[mail.player_email],
            html_message=player_regist_template
        )
        mail.delete()
