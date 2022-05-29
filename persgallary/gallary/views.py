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






def categories_view(request):
    categories = Category.objects.all()

    cxt = {
            'categories': categories,
    }

    return render(request, 'categories.html',cxt)



def view_image(request, pk):
    images = Image.objects.get(id=pk)

    return render(request, 'view_image.html', {'images': images})