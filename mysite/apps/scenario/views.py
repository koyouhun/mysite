# -*- coding:utf-8 -*-

# Python Module
import json

# Django Module
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist

# Third Party Library
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

# Local Module
from mysite.apps.character.models import Character
from mysite.apps.player.models import Player
from .models import Scenario
from .serializer import ScenarioSerializer, ScenarioDetailSerializer


class ScenarioApi(APIView):
    @staticmethod
    def get(request):
        """
        Provide Scenario information
        ---
        response_serializer: ScenarioSerializer
        parameters:
            - name: scenario_id
              required: false
              type: integer
              paramType: query
        """

        if 'id' in request.GET and request.GET['id']:
            data = Scenario.objects.filter(id=request.GET['id'])
        else:
            data = Scenario.objects.all()

        data = ScenarioSerializer(data, many=True).data

        return HttpResponse(JSONRenderer().render(data))


class ScenarioDetailApi(TemplateView):
    template_name = "scenario/scenario_detail.html"

    def get(self, request, *args, **kwargs):
        if 'scenario_id' in kwargs and kwargs['scenario_id']:
            scenario = Scenario.objects.get(pk=kwargs['scenario_id'])
            characters = Character.objects.filter(scenario=kwargs['scenario_id'])
        else:
            raise ValueError("")

        context = self.get_context_data(**kwargs)
        context['characters'] = ScenarioDetailSerializer(characters, many=True).data
        context['scenario'] = ScenarioSerializer(scenario).data

        return self.render_to_response(context)