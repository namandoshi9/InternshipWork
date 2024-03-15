# views.py
from django.shortcuts import render,HttpResponse,redirect
from .form import RegistrationForm
from .models import *

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message or redirect to a success page
            return redirect('show_data') # Change 'success_page' to your actual success page URL
    else:
        form = RegistrationForm()

    return render(request, 'index.html', {'form': form})


def show_data(request):
    data = Registration.objects.all()
    return render(request,'show_data.html',{'data': data})



def deleteView(request, id):
    data = Registration.objects.get(id=id)
    data.delete()
    return redirect('show_data')


def updateView(request,id):
    data = Registration.objects.get(id=id)
    print(data,"RRRRRRRRRRRRR")
    form = RegistrationForm(instance=data)
    if request.method=='POST':
        form = RegistrationForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('show_data')
        
    return render(request, 'index.html', {'form': form, 'data': data})
