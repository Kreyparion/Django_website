from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def reseaux_view(request, *args, **kwargs):
    return render(request, "reseaux.html", {})


def medias_view(request, *args, **kwargs):
    return render(request, "medias.html", {})


def playlist_view(request, *args, **kwargs):
    return render(request, "playlist.html", {})
