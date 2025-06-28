from django.shortcuts import render
def  delete_employee(request,pk):
   EmployeeModel.objects.get(id=pk).delete()
   return render(request,"delete_employee.html")

# Create your views here.
