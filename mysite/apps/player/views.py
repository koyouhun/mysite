# -*- coding:utf-8 -*-

# Python Module

# Django Module
from django.http import HttpResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.db import transaction
from django.conf import settings
from django.core.mail import EmailMessage

# Third Party Library
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from pytz import timezone

# Local Module
from mysite.apps.scenario.models import Scenario
from mysite.apps.player.models import Player
from mysite.apps.character.models import Character
from mysite.templates.email.template import player_regist_template
from .models import Player
from .forms import RegistForm
from .serializer import PlayerSerializer


class Regist(View):
    def get(self, request):
        return HttpResponse("")

    def post(self, request):
        return HttpResponse("")


class PlayerApi(APIView):
    @staticmethod
    def get(request):
        """
        Provide Scenario information
        ---
        response_serializer: PlayerSerializer
        parameters:
            - name: id
              required: false
              type: integer
              paramType: query
        """
        if 'id' in request.GET and request.GET['id']:
            data = Player.objects.filter(id=request.GET['id'])
        else:
            data = Player.objects.all()

        data = PlayerSerializer(data, many=True).data

        return HttpResponse(JSONRenderer().render(data))


class PlayerRegist(TemplateView):
    """
    User Registraion View
    """
    template_name = "player/player_regist.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['scenarios'] = Scenario.objects.filter(is_active=True)
        context['form'] = RegistForm()
        context['success'] = 'GET'

        return self.render_to_response(context)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = RegistForm(request.POST)
        context = self.get_context_data(**kwargs)
        context['success'] = 'POST_SUCCESS'
        context['error'] = "실패 사유"

        if form.is_valid():
            scenario = form.cleaned_data['scenario']

            gender_only = scenario.gender_only
            player_gender = form.cleaned_data['player_gender']
            if gender_only != Scenario.FREE:
                if gender_only == Scenario.MALE_ONLY and player_gender != str(Player.MALE):
                    context['success'] = 'POST_FAIL'
                    context['error'] += "\n남성 전용 시나리오입니다."
                elif gender_only == Scenario.FEMALE_ONLY and player_gender != str(Player.FEMALE):
                    context['success'] = 'POST_FAIL'
                    context['error'] += "\n여성 전용 시나리오입니다."
            if scenario.adult_only == Scenario.YES and form.cleaned_data['player_adult'] != str(Player.YES):
                context['success'] = 'POST_FAIL'
                context['error'] += "\n성인 전용 시나리오입니다."

            character = form.cleaned_data['character']
            if character.status != Character.EMPTY:
                context['success'] = 'POST_FAIL'
                context['error'] += "\n불행! 누군가 캐릭터를 선점 했습니다. 다른 캐릭터를 선택해주세요."

            if context['success'] == 'POST_SUCCESS':
                player = Player.objects.create(
                    name=form.cleaned_data['player_name'],
                    phone_number=form.cleaned_data['player_phone_number'],
                    gender=form.cleaned_data['player_gender'],
                    is_adult=form.cleaned_data['player_adult'],
                    email=form.cleaned_data['player_email']
                )
                player.save()

                character.status = Character.BOOKED
                character.player = player
                character.save()

                data = {'player_name': player.name,
                        'scenario_name': scenario.name,
                        'character_name': character.name,
                        'player_reg_date': player.reg_date.astimezone(timezone('Asia/Seoul')).strftime("%Y/%m/%d, %H:%M")}

                EmailMessage(
                    '[친구따라 강남가자] 신청 확인',
                    player_regist_template % data,
                    to=['koyouhun@daum.net']
                ).send()

                context['form'] = RegistForm
            else:
                context['form'] = form
                context['fail_character'] = Character.objects\
                    .filter(scenario=form.cleaned_data['scenario'])\
                    .filter(status=Character.EMPTY)
        else:
            context['success'] = 'POST_FAIL'
            context['error'] += '잘못된 입력값'
            context['form'] = form
            context['fail_character'] = []

        context['scenarios'] = Scenario.objects.filter(is_active=True)

        return self.render_to_response(context)
