from django.shortcuts import render, get_object_or_404, get_list_or_404
from datetime import datetime
from .models import *


def index(request):
    flowers = Flowers.objects.filter(published=True)

    context = {
        'flowers': flowers,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def types(request, type_id):
    types = get_object_or_404(Types, id=type_id)
    flowers = Flowers.objects.filter(type_id=type_id, published=True)

    context = {
        'types': [types],
        'flowers': flowers,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def flower(request, flower_id):
    flower = get_object_or_404(Flowers, id=flower_id, published=True)

    context = {
        'flower': flower
    }

    return render(request, 'detail.html', context)
