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


def add_details(request):
    form = ImageForm()

    if request.method == 'POST':
        print(request.POST)

        form = ImageForm(request.POST)

        if form.is_valid():
            form.save()


    else:

        form = ImageForm()

    cxt = {
            'form': form,
        }

    return render(request, 'add.html',cxt)




def categories_view(request):
    categories = Category.objects.all()
    details = Image.objects.all()

    cxt = {
            'categories': categories,
            'details': details,
    }

    return render(request, 'categories.html',cxt)



def view_image(request, pk):
    images = Image.objects.get(id=pk)

    return render(request, 'view_image.html', {'images': images})