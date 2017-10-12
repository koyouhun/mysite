# -*- coding:utf-8 -*-

# Python Module

# Django Module
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.db import transaction
from django.apps import apps

# Third Party Library
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

# Local Module

# Inner Module
from .models import Player
from .forms import RegistForm, CancelForm
from .serializer import PlayerSerializer

# Local Model
Scenario = apps.get_app_config('scenario').get_model('Scenario')
Character = apps.get_app_config('character').get_model('Character')
Mail = apps.get_app_config('mail').get_model('Mail')


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
                    nickname=form.cleaned_data['player_nickname'],
                    phone_number=form.cleaned_data['player_phone_number'],
                    gender=form.cleaned_data['player_gender'],
                    is_adult=form.cleaned_data['player_adult'],
                    email=form.cleaned_data['player_email']
                )
                player.save()

                character.status = Character.BOOKED
                character.player = player
                character.save()

                mail = Mail.objects.create(
                    player_name=player.name,
                    scenario_name=scenario.name,
                    character_name=character.name,
                    player_reg_date=player.reg_date,
                    player_email=player.email
                )
                mail.save()

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


class RegistCancel(TemplateView):
    """
    Regist Cancel View
    """
    template_name = "player/regist_cancel.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        scenario = Scenario.objects.get(id=kwargs['scenario_id'])
        context['scenario'] = scenario
        context['characters'] = scenario.character.filter(status=Character.BOOKED)
        context['form'] = CancelForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = CancelForm(request.POST)
        context = self.get_context_data(**kwargs)
        context['success'] = "입력칸을 채워주세요!"
        scenario = Scenario.objects.get(id=request.POST['scenario_id'])
        if form.is_valid():
            character = Character.objects.get(id=form.cleaned_data['character_id'])
            player = character.player
            context['success'] = "정보가 일치하지 않습니다"
            if form.cleaned_data['player_email'] == player.email and \
                form.cleaned_data['player_name'] == player.name and \
                form.cleaned_data['player_phone_number'] == player.phone_number:
                player.delete()
                character.player = None
                character.status = Character.EMPTY
                character.save()
                context['success'] = "취소됐습니다!"
                return HttpResponseRedirect('/')
        context['scenario'] = scenario
        context['characters'] = scenario.character.filter(status=Character.BOOKED)
        context['form'] = form
        return self.render_to_response(context)
