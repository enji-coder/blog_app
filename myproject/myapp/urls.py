from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('upload/',views.upload,name="upload"),
    path('uploadpic/',views.uploadpic,name="uploadpic"),
    path('gallery/',views.gallery,name="gallery"),
    path('uploadvideo/',views.uploadvideo,name="uploadvideo"),
    path('videoview/',views.videoview,name="videoview"),
    path('uploadaudio/',views.uploadaudio,name="uploadaudio"),
    path('audioview/',views.audioview,name="audioview"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)