from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from paras.models import Employee

# Create your views here.
def emp_detail(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    context = {'emp' : emp,}
    return render(request, 'emp_details.html', context)
    
