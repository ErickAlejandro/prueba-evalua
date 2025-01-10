from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getTargetNum/', views.get_target_num, name='getTargetNum'),
]
