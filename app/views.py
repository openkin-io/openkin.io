from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from .models import Person, Filiation
import json

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


def family_tree_api(request):
    if request.method == "GET":
        persons = list(Person.objects.values('id', 'given_name', 'surname', 'birth_date'))
        filiation = list(Filiation.objects.values('child', 'child_id', 'parent'))
        return JsonResponse({'persons': persons, 'filiation': filiation})
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)
            new_person = Person.objects.create(
                given_name=data.get('given_name'),
                surname=data.get('surname'),
                birth_date=data.get('birth_date')
        )
            return JsonResponse({
                'message': 'Person created', 
                'id': new_person.id,
                'given_name': new_person.given_name,
                'surname': new_person.surname,
                'birth_date': new_person.birth_date
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            print(str(e))
            return JsonResponse({'error': str(e)}, status=500)

