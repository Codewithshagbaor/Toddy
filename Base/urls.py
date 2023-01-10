from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('delete/<str:uid>', views.delete_view, name="delete"),
]