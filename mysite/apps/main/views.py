from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject
# Create your views here.


def home(request):
    # return HttpResponse('Hello World!')
    return render(request=request, template_name="main/home.html", context={'subject': Subject.objects.all})