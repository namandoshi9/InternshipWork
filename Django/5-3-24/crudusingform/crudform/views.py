from django.shortcuts import render, redirect
from .models import Employee
from .form import EmployeeForm
from django.contrib import messages

# Create your views here.
def addemployeeView(request):
    form = EmployeeForm()
    all_employee = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'form submission sucessful')
            return redirect('/')
        
    context = {
        'form' : form,
        'all_employee' : all_employee,
    }
    return render(request, 'index.html', context)


def updateemployeeView(request, id):
    emp = Employee.objects.get(id=id)
    all_employee = Employee.objects.all()
    form = EmployeeForm(instance=emp)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            messages.info(request,'data Update sucessful')
            return redirect('/')
    context = {"form": form, "all_employee": all_employee}
    return render(request, 'index.html', context)


def deleteemployeeView(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    messages.error(request,'data Update sucessful')

    return redirect('/')