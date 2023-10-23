from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home, name="Home"),
    path("about", views.about, name="about"),
    path("courses", views.courses, name="courses"),
    path("contacts", views.contacts, name="contacts"),
    path("directions", views.directions, name="directions"),
]
