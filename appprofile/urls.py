from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.homepage),
    path('event_detail/<int:event_id>', views.event_detail, name='Event_Detail'),
    path('message/',views.message),
    path('gallery/', views.gallerypage),
    path('terms/', views.terms_page),
    path('privacy_policy/', views.privacy_policy_page),
    path('applogin/',views.applogin, name='applogin'),
    path('login/',views.weblogin, name='login'),
    #url(r'^send_otp/',views.send_otp),
    url(r'^retry_otp',views.retry_otp),
    url(r'^login/facebook',views.login_fb),
    path('verify_otp/',views.verify_otp),
    path('appregister/', views.appregister, name='appregister'),
    path('register/', views.webregister, name='register'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    #url(r'^dashboard/',views.dashboard),
]