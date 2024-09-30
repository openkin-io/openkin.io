from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("familytree/", views.familytree, name="familytree"),
    path("faq/", views.faq, name="faq"),
    path("learn/", views.learn, name="learn"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("api/familytree/", views.family_tree_api, name="family_tree_api"),
]
