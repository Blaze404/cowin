from django.urls import path
from . import views

app_name = 'Cowin Notification'


urlpatterns = [
    path('', views.index, name="homepage"),
    path('getVaccine/', views.get_vaccine, name="get_vaccine"),
    path('saveNotify/', views.update_notification, name='update_notification'),
    path('notAvailable/', views.not_available, name='update_notification'),
    path('showAll/', views.show_all, name='show_all'),
    path('ping/', views.ping, name='ping')
]
