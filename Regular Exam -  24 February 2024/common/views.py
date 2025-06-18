from django.shortcuts import render
from django.views.generic import TemplateView

from DjangoProject.utils import get_profile


# Create your views here.
# def index(request):
#     profile = get_profile()
#
#     context = {
#         'profile': profile,
#     }
#     return render(request, 'common/index.html', context)

class IndexView(TemplateView):
    template_name = 'common/index.html'

