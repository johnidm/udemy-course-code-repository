from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index-challenge"),
    path("<int:month>", views.monthly_by_id, name="month-challenge-by-name"),
    path("<str:month>", views.monthly, name="month-challenge"),
]
