from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from django.shortcuts import redirect
from .models import Employee,DeletedEmployee
from django.http import JsonResponse


#create view
def Create_employee(request):
     if request.method=="POST" :
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('list')
     else:
        form =EmployeeForm()
     return render(request,'create.html',{'form':form})



def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', {'employees': employees})

def update_employee(request,pk):
    employee=Employee.objects.get(id=pk)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=EmployeeForm(instance=employee)
    return render(request,'update.html',{'form':form})






def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    # Save to DeletedEmployee before deleting
    DeletedEmployee.objects.create(
        employee_id=employee.employee_id,
        employee_name=employee.employee_name,
        employee_email=employee.employee_email,
        employee_contact=employee.employee_contact,
    )

    employee.delete()
    return redirect('list')

def deleted_history(request):
    deleted_employees = DeletedEmployee.objects.all().order_by('-deleted_at')
    return render(request, 'deleted_history.html', {'deleted_employees': deleted_employees})


def search_employee(request):
    query = request.GET.get('q', '').strip().lower()
    if query:
        # Get IDs of deleted employees to exclude them
        deleted_ids = DeletedEmployee.objects.values_list('employee_id', flat=True)

        # Search by name or ID, excluding deleted ones
        employees = Employee.objects.filter(
            employee_name__icontains=query
        ).exclude(employee_id__in=deleted_ids)

        if employees.exists():
            employee_list = [
                {
                    "employee_id": e.employee_id,
                    "employee_name": e.employee_name,
                    "employee_email": e.employee_email,
                    "employee_contact": e.employee_contact,
                }
                for e in employees
            ]
            return JsonResponse({"success": True, "employees": employee_list})
        else:
            return JsonResponse({"success": False, "message": "No matching active employee found."})
    return JsonResponse({"success": False, "message": "Empty search query."})