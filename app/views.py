from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    return render(request, "pages/index.html", {"page_title": _("Home")})


def about(request):
    return render(request, "pages/about.html", {"page_title": _("About")})


def contact(request):
    return render(request, "pages/contact.html", {"page_title": _("Contact")})


def familytree(request):
    return render(request, "pages/familytree.html", {"page_title": _("Family Tree")})


def faq(request):
    return render(request, "pages/faq.html", {"page_title": _("FAQ")})


def learn(request):
    return render(request, "pages/learn.html", {"page_title": _("Learn")})


def privacy(request):
    return render(request, "pages/privacy.html", {"page_title": _("Privacy Policy")})


def terms(request):
    return render(request, "pages/terms.html", {"page_title": _("Terms & Conditions")})
