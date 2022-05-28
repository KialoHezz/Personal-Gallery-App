from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def home_view(request):

    return render(request, 'home.html')


def about_view(request):

    return render(request, 'about.html')


def travel_view(request):

    return render(request, 'travel.html')

def food_view(request):

    return render(request, 'food.html')