from django.urls import path
from . import views

app_name = 'bog'

urlpatterns=[
	path('board4/', views.board, name='board4'),
]