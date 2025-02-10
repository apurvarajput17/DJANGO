from django.urls import path

from .views import addview,sview

urlpatterns=[
    path("av/",addview),
    path("sv/",sview)
]

