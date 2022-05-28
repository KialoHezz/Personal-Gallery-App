from django.shortcuts import render
from gallary.models import (Image,Location,Category)
from gallary.forms import ImageForm

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


def add_travel(request):
    form = ImageForm()

    if request.method == 'POST':
        print(request.POST)
        form = ImageForm(request.POST)


        if form.is_valid():
            form.save()

        return render('travel')

    else:

        form = ImageForm(request.POST)

    context = {
        'form': form
    }

    return render(request, 'add_travel.html', context=context)


def category(request):

    categories = Category.objects.all()

    cxt = {
            'categories': categories,
            'images': images,
    }

    return render(request, 'travel.html',cxt)


def view_image(request, pk):
    images = Image.objects.get(id=pk)

    return render(request, 'view_image.html', {'images': images})