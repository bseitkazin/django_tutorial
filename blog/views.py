from django.http import Http404
from django.shortcuts import render
from .models import Album

# Create your views here.
def index(request):
	all_albums = Album.objects.all()
	return render(request, 'blog/index.html', {'all_albums' : all_albums})

def detail(request, blog_id):
	try:
		album = Album.objects.get(pk = blog_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exist")
	return render(request, 'blog/detail.html', {'album' : album})