from django.conf.urls import url, include
from . import views
from django.urls import path

app_name='speaker'

urlpatterns = [
    path('list/', views.get_speakers),
    url(r'^$', views.post_speakers, name='Post_Speakers'),
    path('new_speaker/add',views.add_speakers, name='add_speakers'),
    path('new_speaker',views.new_speaker),
    path('retrieve',views.retrieve_speakers)
    #path('view/<int:id>/', views.view_speaker)
]
