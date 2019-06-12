from django.shortcuts import render
from django.http import HttpResponse
from .models import * 

# Create your views here.
def index(request):
    return render(request,"myapp/index.html")
    
def upload(request):
    return render(request,"myapp/uploadpicture.html")

def uploadpic(request):
    obj=pictures()
    obj.pic=request.FILES['pic']
    insert=pictures.objects.create(pic=obj.pic)
    print("-----------> picture uploaded")
    getall=pictures.objects.all()
    return render(request,"myapp/gallery.html",{'getall':getall})

def gallery(request):
    getall=pictures.objects.all()
    return render(request,"myapp/gallery.html",{'getall':getall})

def uploadvideo(request):
    obj=videos()
    obj.name=request.POST['videoname']
    obj.videofile=request.FILES['video']
    insert=videos.objects.create(videofile=obj.videofile)
    return render(request,"myapp/index.html")

def videoview(request): 
    """
    display all videos
    #obj=videos.objects.all()
    #return render(request,"myapp/videoview.html",{'obj':obj})
    """
    obj=videos.objects.last()
    print("------------>",obj)
    return render(request,"myapp/videoview.html",{'obj':obj})
    
def uploadaudio(request):
    obj=Song()
    obj.name=request.POST['audioname']
    obj.audiofile=request.FILES['audiofile']
    insert=Song.objects.create(songname=obj.name,audiofile=obj.audiofile)
    return render(request,"myapp/index.html")

def audioview(request):
    obj=Song.objects.all()
    return render(request,"myapp/audioview.html",{'obj':obj})
    
