from django.db import models



from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField()
    employee_contact = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # New field

    def __str__(self):
        return self.employee_name

    
    

class DeletedEmployee(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField()
    employee_contact = models.CharField(max_length=20)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_name
