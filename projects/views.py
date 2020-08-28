from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def projects_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'projects_list.html', {}) 
