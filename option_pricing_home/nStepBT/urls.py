from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='Nstep-home'),
    path("empty/<str:value>/<str:p_value>/<str:n>/<str:S0>/<str:sigma>/<str:r>/<str:T>/<str:K>/", views.empty),
]