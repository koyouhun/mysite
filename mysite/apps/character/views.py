# -*- coding:utf-8 -*-

# Python Module

# Django Module
from django.http import HttpResponse

# Third Party Library
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

# Local Module
from .models import Character
from .serializer import CharacterSerializer

# Inner Module


class CharacterApi(APIView):
    @staticmethod
    def get(request):
        """
        hello
        ---
        response_serializer: CharacterSerializer
        parameters:
            - name: id
              required: false
              type: integer
              paramType: query
        """
        if 'id' in request.GET and request.GET['id']:
            data = Character.objects.filter(id=request.GET['id'])
        elif 'scenario_id' in request.GET and request.GET['scenario_id']:
            data = Character.objects.filter(
                scenario=request.GET['scenario_id'],
                status=Character.EMPTY
            )
        else:
            data = Character.objects.all()

        data = CharacterSerializer(data, many=True).data

        return HttpResponse(JSONRenderer().render(data))

    @staticmethod
    def post(self):
        """
        hello
        ---
        response_serializer: CharacterSerializer
        parameters:
            - name: id
              required: false
              type: integer
              paramType: query
        """
        pass
