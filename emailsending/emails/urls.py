from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^email_one/$', views.email_one, name='email_one'),
    url(r'^email_two/$', views.email_two, name='email_two')
]