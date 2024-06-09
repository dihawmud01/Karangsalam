from django.shortcuts import render, get_object_or_404
from .models import Destinations, Fasility, Profile
from django.http import Http404
import requests
from django.db.models import Q


def simple_render_semua_destinasi(request):
    destinasi = Destinations.objects.all()
    print(destinasi)
    facilities = Fasility.objects.select_related('destination').all()
    print(facilities)

    return render(request, 'detinasi.html', {'destinasi': destinasi, 'facilities': facilities})


def profile(request):
    profile = Profile.objects.all()
    print(profile)

    def __str__(self):
        return self.name
    return render(request, 'profile.html', {'profile': profile})


def index(request):
    return render(request, 'index.html')


def destination(request):
    destinations = Destinations.objects.all()
    return render(request, 'destination.html', {'destinations': destinations})


def destinationProfile(request, id):
    try:
        destination = Destinations.objects.get(id=id)
        destination = get_object_or_404(Destinations, pk=id)
        facilities = destination.fasility_set.all()
    except Destinations.DoesNotExist:
        raise Http404("Destination does not exist")

    # Lakukan operasi lain yang Anda inginkan dengan objek Destination

    return render(request, 'destprofile.html', {'destination': destination, 'facilities': facilities})


def search(request):
    # Get the value of 'q' key or provide an empty string as default
    query = request.GET.get('q', '')
    if query:
        data = Destinations.objects.filter(
            Q(nama__icontains=query) |  # Search by name
            Q(kategori__icontains=query) |  # Search by category
            Q(location__icontains=query)  # Search by location
        )
    else:
        data = Destinations.objects.all()
    context = {
        'data': data,
        'query': query,
    }
    return render(request, 'search.html', context)
