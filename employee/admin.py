from django.contrib import admin
from .models import Employee, DeletedEmployee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_email', 'created_at')

    # Custom delete logic for admin delete
    def delete_model(self, request, obj):
        # Save to DeletedEmployee before deleting
        DeletedEmployee.objects.create(
            employee_id=obj.employee_id,
            employee_name=obj.employee_name,
            employee_email=obj.employee_email,
            employee_contact=obj.employee_contact
        )
        obj.delete()

admin.site.register(Employee, EmployeeAdmin)


@admin.register(DeletedEmployee)
class DeletedEmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_email', 'deleted_at')


