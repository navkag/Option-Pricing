from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='normalDist-home'),
    path("empty/<str:value>/<str:p_value>/<str:S0>/<str:sigma>/<str:r>/<str:T>/<str:K>/", views.empty),
]
