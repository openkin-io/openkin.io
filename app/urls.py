from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("services/", views.services, name="services"),
    path("technologies/", views.tech, name="tech"),
    path("about/", views.about, name="about"),
    # path("contact/", views.contact, name="contact"),
]
