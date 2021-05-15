from django.urls import path
from . import views

app_name = 'Cowin Notification'


urlpatterns = [
    path('', views.index, name="homepage"),
    path('m/', views.index_marathi, name="homepage"),
    path('h/', views.index_hindi, name="homepage"),
    path('getVaccine/', views.get_vaccine, name="get_vaccine"),
    path('m/getVaccine/', views.get_vaccine_marathi, name="get_vaccine"),
    path('h/getVaccine/', views.get_vaccine_hindi, name="get_vaccine"),
    path('saveNotify/', views.update_notification, name='update_notification'),
    path('m/saveNotify/', views.update_notification_marathi, name='update_notification'),
    path('h/saveNotify/', views.update_notification_hindi, name='update_notification'),
    path('notAvailable/', views.not_available, name='update_notification'),
    path('showAll/', views.show_all, name='show_all'),
    path('ping/', views.ping, name='ping'),

]
