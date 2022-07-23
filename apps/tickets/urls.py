from django.urls import path

from apps.tickets import views


urlpatterns = [
    path('/', views.home_page, name='home'),
]
