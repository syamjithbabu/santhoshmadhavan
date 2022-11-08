from django.shortcuts import render

from web.models import Gallery

# Create your views here.

def index(request):
    gallery_image = Gallery.objects.all().order_by('id')[:4]
    context = {
    'gallery' : gallery_image
    }
    return render(request,"web/index.html",context)

def gallery(request):
    gallery_image = Gallery.objects.all()
    context = {
        'gallery' : gallery_image
    }
    return render(request,"web/gallery.html",context)