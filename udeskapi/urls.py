from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = '[udeskapi]'
urlpatterns = [
    path('', views.home),
    path('cc_force_api/', views.cc_force_api, name='cc_force_api'),
    path('call1/', views.call1, name='call1'),
    path('call2/', views.call2, name='call2'),
    path('call3/', views.call3, name='call3'),
    path('call4/', views.call4, name='call4'),
    path('call5/', views.call5, name='call5'),
    path('call6/', views.call6, name='call6'),
    path('call7/', views.call7, name='call7'),
    path('call8/', views.call8, name='call8'),
    path('call9/', views.call9, name='call9'),
    path('call10/', views.call10, name='call10'),
    path('call11/', views.call11, name='call11'),
    path('call12/', views.call12, name='call12'),
    path('call13/', views.call13, name='call13'),
    path('call14/', views.call14, name='call14'),
    path('call15/', views.call15, name='call15'),
    path('call16/', views.call16, name='call16'),
    path('agent1/', views.agent1, name='agent1'),
    path('agent2/', views.agent2, name='agent2'),
    path('agent3/', views.agent3, name='agent3'),
    path('agent4/', views.agent4, name='agent4'),
    path('agent5/', views.agent5, name='agent5'),
    path('agent6/', views.agent6, name='agent6'),
    path('user_group1/', views.user_group1, name='user_group1'),
    path('user_group2/', views.user_group2, name='user_group2'),
    path('user_group3/', views.user_group3, name='user_group3'),
    path('user_group4/', views.user_group4, name='user_group4'),
    path('user_group5/', views.user_group5, name='user_group5'),
    path('callcenter_analysis1/', views.callcenter_analysis1, name='callcenter_analysis1'),
    path('callcenter_analysis2/', views.callcenter_analysis2, name='callcenter_analysis2'),
    path('callcenter_analysis3/', views.callcenter_analysis3, name='callcenter_analysis3'),
    path('callcenter_analysis4/', views.callcenter_analysis4, name='callcenter_analysis4'),
    path('custom_fields1/', views.custom_fields1, name='custom_fields1'),
    path('custom_fields2/', views.custom_fields2, name='custom_fields2'),
    path('organizations1/', views.organizations1, name='organizations1'),
    path('organizations2/', views.organizations2, name='organizations2'),
    path('organizations3/', views.organizations3, name='organizations3'),
    path('organizations4/', views.organizations4, name='organizations4'),
    path('organizations5/', views.organizations5, name='organizations5'),
    path('organizations6/', views.organizations6, name='organizations6'),
    path('customers3/', views.customers3, name='customers3'),

]
urlpatterns += staticfiles_urlpatterns()