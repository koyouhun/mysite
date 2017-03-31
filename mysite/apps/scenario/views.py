# -*- coding:utf-8 -*-

# Python Module

# Django Module
from django.http import HttpResponse

# Third Party Library
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

# Local Module

# Inner Module
from .models import Scenario
from .serializer import ScenarioSerializer


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