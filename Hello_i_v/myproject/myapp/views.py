from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import EmployeeModel  
from .forms import EmployeeForm

def insert_employee(request):
    context ={}
    ob_form = EmployeeForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_employee.html", context) 
def view_employee(request):
    ob=EmployeeModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_employee.html')
    return HttpResponse(temp.render(context,request))

def delete_employee(request,pk):
    ob=EmployeeModel.objects.get(id=pk).delete()
    return render(request,"delete_employee.html")

from django.shortcuts import get_object_or_404, redirect
def update_employee(request,pk):
    obe = get_object_or_404(EmployeeModel, id=pk)
    if request.method == 'POST':
        obf = EmployeeForm(request.POST, instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('view_employee')#, id=pk
    else:
        formdata=EmployeeForm(instance=obe)
    return render(request, "update_employee.html", {'form':formdata})

    

