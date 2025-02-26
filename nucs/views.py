from django.http import HttpResponse, HttpRequest
from datetime import datetime
from django.shortcuts import render

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'nucs/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'nucs/contact.html',
        {
            'title':'Contact',
            'message':'Contact Info will be displayed here.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'nucs/about.html',
        {
            'title':'About',
            'message':'About',
            'year':datetime.now().year,
        }
    )
