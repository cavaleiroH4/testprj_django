from django.shortcuts import render


def home(request):
    return render(request, 'templates/recipes/pages/home.html')


# Create your views here.
