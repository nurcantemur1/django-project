from django.shortcuts import render
from .models import Category

# kategorilist=["1","2","3","4"]
movielist=[
    {"id":1,"name":"film1", "descriptions":"aa" ,"image":"app-logo.png"},
    {"id":2,"name":"film2", "descriptions":"aa" ,"image":"app-logo.png"},
    {"id":3,"name":"film3", "descriptions":"aa" ,"image":"app-logo.png"},
    {"id":4,"name":"film4", "descriptions":"aa" ,"image":"app-logo.png"},
    {"id":5,"name":"film5", "descriptions":"aa" ,"image":"app-logo.png"},


]

# Create your views here.
def home(request):
    data={
        # "kategoriler":kategorilist,
        "kategoriler":Category.objects.all(),
        "movies":movielist
    }
    return render(request,"index.html",data)

def movies(request):
    return render(request,"movies.html")

def moviedetail(request,id):
    data={
        "id":id
    }
    return render(request,"details.html",data)

