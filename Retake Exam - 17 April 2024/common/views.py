from django.shortcuts import render
from django.views import View


# Create your views here.
def homepage_view(request):

    return render(request,"common/home-page.html")

