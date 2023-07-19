from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.home, name='homepage'),
    path("2step/", include('twoStepBT.urls')),
    path("Nstep/", include('nStepBT.urls')),
    path("normalDist/", include('normalDist.urls')),
]

urlpatterns += staticfiles_urlpatterns()
