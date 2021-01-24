"""
Urls for apk app.

"""

from django.urls import path
from apk.views import home_page
from apk.views import game_page

urlpatterns = [
    path('', home_page, name='home'),
    path('UmoSpace', game_page, name='game')
]