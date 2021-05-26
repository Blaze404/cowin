from django.urls import path
from . import views

app_name = 'Agent Stat'


urlpatterns = [
    path('', views.index, name="homepage"),
    path('add/', views.add, name="add"),
    path('agent/', views.add_agent, name="add_agent"),
    path('all/', views.show_all, name='show_all'),
    path('/stats/', views.stats, name='stats')
]
