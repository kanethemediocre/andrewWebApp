"""
Urls for apk app.

"""

from django.urls import path
from apk.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
]