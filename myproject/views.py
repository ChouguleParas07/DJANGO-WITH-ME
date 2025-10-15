from django.http import HttpResponse
from django.shortcuts import render
from paras.models import Employee

def home(request):
    paras = Employee.objects.all()
    context = {'paras': paras, }
    return render(request, 'index.html', context)

