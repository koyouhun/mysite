from pytz import timezone
from django.core.mail import EmailMessage
from django.db import transaction

from mysite.templates.email.template import player_regist_template
from .models import Mail


@transaction.atomic
def email_sending():
    mails = Mail.objects.all()

    for mail in mails:
        data = {'player_name': mail.player_name,
                'scenario_name': mail.scenario_name,
                'character_name': mail.character_name,
                'player_reg_date': mail.player_reg_date.astimezone(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M")}

        EmailMessage(
            '[친구따라 강남가자] 신청 확인',
            player_regist_template % data,
            to=[mail.player_email]
        ).send()

        mail.delete()
