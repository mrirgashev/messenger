from django.urls import path
from . import views


app_name = 'messeneger' 
urlpatterns = [
    path('', views.home, name='home'),
    path('chat/<int:receiver_id>/', views.chat, name='chat'),
]