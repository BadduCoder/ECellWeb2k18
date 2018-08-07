"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from server import settings as sett
from django.conf.urls import url
from django.views import static as stat
from appprofile import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/',views.login, name='login'),
    #path('register/', views.register, name='register'),
    url(r'^settings/$',views.social_settings, name='settings'),
    url(r'^settings/password/$',views.password, name='password'),
    path('',include('appprofile.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('event/', include('events.urls')),
    path('sponsor/', include('sponsors.urls')),
    path('mentor/', include('mentors.urls')),
    path('startup/', include('startups.urls')),
    path('speaker/', include('speakers.urls')),
    path('message/', include('contactus.urls')),
    path('quiz/', include('bquiz.urls')),
    path('team/',include('team.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^password_reset/$', auth_views.password_reset),
    url(r'^password_reset/done/$', auth_views.password_reset_done),
    url(r'^reset/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm),
    url(r'^reset/done/$', auth_views.password_reset_complete),
    url(r'^add/(\d+)/$', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)/$', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/',views.bag, name='cart'),
    url(r'^static/(?P<path>.*)$', stat.serve, {'document_root': settings.STATIC_ROOT}),

]

admin.site.site_header = settings.SITE_HEADER
