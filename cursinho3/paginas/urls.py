from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'paginas'),
    path('sobre/', views.sobre, name= 'sobre'),
]