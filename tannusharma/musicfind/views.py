from django.shortcuts import render
from .models import Music
# Create your views here.
def home(request):
    music=Music.objects.all()
    s=request.GET.get('song')
    a=request.GET.get('artist')
    al=request.GET.get('album')
    y=request.GET.get('year')
    
    if s:
        music=music.filter(song__icontains=s)
    if a:
        music=music.filter(artist__icontains=a)
    if al:
        music=music.filter(album__icontains=al)
    if y:
        music=music.filter(year=y)
    return render(request,'1.html',{"music":music})