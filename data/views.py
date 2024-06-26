from django.shortcuts import render
from .models import movie_list

def index(request):
    obj=movie_list.objects.all()
    return render(request, 'home.html',{"obj":obj})

def create(request):
    if request.method == "POST":
        moviename = request.POST.get("Moviename",'')
        year = request.POST.get("year",'')
        rating = request.POST.get("rating",'')
        obj = movie_list(name=moviename, year=year, rating=rating)
        obj.save()
    return render(request, "create.html")


def edit(request, pk):
    edited = movie_list.objects.get(pk=pk)
    if request.method == "POST":
        edited.name = request.POST.get("Moviename",'')
        edited.year = request.POST.get("year",'')
        edited.rating = request.POST.get("rating",'')
        edited.save()
    return render(request, "edit.html", {"movie": edited})

def delete(request, pk):
    deleted = movie_list.objects.get(pk=pk)
    if request.method == "POST":
        deleted.delete()
    return render(request, "delete.html")

def base (request):
    return render(request, 'base.html')

def menu (request):
    return render(request, 'menu.html')

def first (request):
    return render(request, 'first.html')
