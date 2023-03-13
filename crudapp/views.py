from datetime import date

from django.shortcuts import HttpResponseRedirect, render
from django.utils import timezone

from .models import Employee

created_date = timezone.now()
# from django.views import View


# class MyView(View):
#     def get(self, request):
#         all_employee = Employee.objects.all()
#         return render(request, 'index.html', {"data":all_employee})

def getEmployee(request):
    all_employee = Employee.objects.all()
    print(all_employee, "ALALL \n\n\n\n")
    return render(request, 'index.html', {"data":all_employee})

def newEmployee(request):
    if(request.method=="POST"):
        msg = "Please enter valid number."
        add = Employee()
        add.first_name = request.POST.get('first_name')
        add.last_name = request.POST.get('last_name')
        number = request.POST.get('phone')
        if len(number) == 10:
            add.phone = request.POST.get('phone')
        else:
            return render(request, 'newemployee.html', {'message': msg})
        add.email = request.POST.get('email')
        add.designation = request.POST.get('desg')
        add.created_on = created_date
        add.location = request.POST.get('location')
        add.save()
        return HttpResponseRedirect('/')

    return render(request, 'newemployee.html')

def updateEmployee(request, id):
    update = Employee.objects.get(id=id)
    msg = "Please enter valid number."
    if request.method=='POST':
        update.first_name = request.POST.get('first_name')
        update.last_name = request.POST.get('last_name')
        valid = request.POST.get('phone')
        if len(valid) == 10:
            update.phone = request.POST.get('phone')
        else:
            return render(request, 'update.html', {"message": msg})
        update.email = request.POST.get('email')
        update.designation = request.POST.get('desg')
        update.location = request.POST.get('location')
        update.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {"update": update})

def deleteEmployee(request, id):
    deleteData = Employee.objects.get(id=id)
    try:
        if deleteData:
            deleteData.delete()
            return HttpResponseRedirect('/')
    except Exception as e:
        print(e, f"/n {deleteData} Dose not exist.")


