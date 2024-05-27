from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    return render(request, "pages/index.html", {"page_title": _("Home")})
def about(request):
    return render(request, "pages/about.html", {"page_title": _("About")})
