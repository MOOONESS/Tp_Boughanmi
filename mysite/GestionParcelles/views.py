from django.shortcuts import render
from .models import Parcelles

def map_view(request):
    parcelles = Parcelles.objects.all()
    return render(request, 'map.html', {'parcelles': parcelles})
