# notice_board_app/urls.py

from django.urls import path
from . import views

app_name = 'notice_board_app'

urlpatterns = [
    path('', views.notice_list, name='notice_list'),  # Notice the URL pattern here
    path('<int:pk>/', views.notice_detail, name='notice_detail'),
]
