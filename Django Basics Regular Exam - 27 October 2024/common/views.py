from django.shortcuts import render
from django.views.generic import ListView

from post.models import Post


# Create your views here.
def index(request):
    return render(request, 'common/index.html')

class Dashboard(ListView):
    model = Post
    template_name = 'common/dashboard.html'
