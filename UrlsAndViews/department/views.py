from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from department.models import Department


# Create your views here.
def index(request):
    return HttpResponse("<h1>Departments home page</h1>")

def int_param_view(request, pk:int):
    return HttpResponse(f"<h1>Department index: {pk}</h1>")

def str_param_view(request, name):
    return HttpResponse(f"<h1>Department name: {name}</h1>")

def slug_param_view(request, slug):
    # department = Department.objects.filter(slug=slug).first()

    department = get_object_or_404(Department, slug=slug)
    return render(request,"slug_template.html",{"department":department})

def file_path_param_view(request, path_to_file):
    return HttpResponse(f"<h1>The file is located at: {path_to_file}</h1>")

def uuid_param_view(request, id):
    return HttpResponse(f"<h1>The uuid is: {id}</h1>")

def regex_view(request, archive_year:int):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")

def contacts_view(request):
    return HttpResponse(f"<h1>We are departments</h1>")

def about_view(request):
    return redirect('int_view', pk=123, permanent=True)
