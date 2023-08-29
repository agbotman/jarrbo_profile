from django.conf.urls import include, url
from django.contrib import admin
from .views import jarrbo_home, ContactView, ThanksView, ProfileView

urlpatterns = [
    url(r'^$', jarrbo_home, name='jarrbo_home'),
    url(r'^contact/$', ContactView, name='contact'),
    url(r'^contact/thanks', ThanksView, name='thanks'),
    url(r'^profile/$', ProfileView, name='profile'),
]
