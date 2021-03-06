"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from .apps.character.views import CharacterApi
from .apps.player.views import PlayerApi, PlayerRegist, RegistCancel
from .apps.scenario.views import ScenarioApi

urlpatterns = [
    url(r'^$', PlayerRegist.as_view(), name="regist"),
    url(r'^cancel/(?P<scenario_id>[0-9]+)$', RegistCancel.as_view(), name="cancel"),
    #url(r'^api/scenario/(?P<scenario_id>[0-9]+)$', ScenarioDetailApi.as_view()),
    url(r'^api/character$', CharacterApi.as_view()),
    url(r'^api/player', PlayerApi.as_view()),
    url(r'^api/scenario', ScenarioApi.as_view()),
    url(r'^admin/', admin.site.urls),
]
