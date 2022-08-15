from django.shortcuts import render
from .models import Usermodel
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def userpage(request):
    if request.method=='POST':
        userdata=Usermodel()
        userdata.username=request.POST.get('uname')
        userdata.usermail=request.POST.get('uemail')
        userdata.pwd=request.POST.get('upwd')
        userdata.maritialstatus=request.POST.get('mstatus')
        userdata.gender=request.POST.get('gender')
        userdata.save()
        messages.success(request,'New Userdata Saved Succesfully!!')
        return render(request,'index.html')
    else:
        return render(request,'index.html')
def view_emp(request):
    all_data=Usermodel.objects.all()
    return render(request,'view_emp.html',{'all_data':all_data})
def delete(request,emp_id=0):
    if emp_id:
        all_data=Usermodel.objects.get(id=emp_id)
        all_data.delete()
        return HttpResponse('User removed succesfully')
def edit(request,emp_id=0):
    if request.method=='POST':
        if emp_id:
            userdata=Usermodel.objects.get(id=emp_id)
            userdata.username=request.POST.get('uname')
            userdata.usermail=request.POST.get('uemail')
            userdata.pwd=request.POST.get('upwd')
            userdata.maritialstatus=request.POST.get('mstatus')
            userdata.gender=request.POST.get('gender')
            userdata.save()
            messages.success(request,'Userdata Updated Succesfully!!')
            return HttpResponse("user updated succesfully")
    else:
        if emp_id:
            edit_data=Usermodel.objects.get(id=emp_id)
            return render(request,'edit.html',{'edit_data': edit_data})


    