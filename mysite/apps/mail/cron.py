from django.core import mail as dj_mail
from django.conf import settings

from mysite.templates.email.template import player_regist_template
from .models import Mail


def email_sending():
    mails = Mail.objects.all()

    for mail in mails:
        data = {'player_name': mail.player_name, }
                # 'scenario_name': mail.scenario_name,
                # 'player_reg_date': mail.player_reg_date.astimezone(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M")}

        dj_mail.send_mail(
            subject='[게임데이] 신청 확인',
            message=player_regist_template % data,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[mail.player_email],
            html_message=player_regist_template % data
        )

        mail.delete()
