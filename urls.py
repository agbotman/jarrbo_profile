from django.urls import re_path
from django.contrib import admin
from .views import jarrbo_home, ContactView, ThanksView, ProfileView

urlpatterns = [
    re_path(r'^$', jarrbo_home, name='jarrbo_home'),
    re_path(r'^contact/$', ContactView, name='contact'),
    re_path(r'^contact/thanks', ThanksView, name='thanks'),
    re_path(r'^profile/$', ProfileView, name='profile'),
]
