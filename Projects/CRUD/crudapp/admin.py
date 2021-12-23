from django.contrib import admin
from crudapp.models import Employees

# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    '''
        Admin view for employee
    '''
    list_display = ['id', 'eno', 'ename', 'esalary', 'eaddress']

admin.site.register(Employees, EmployeesAdmin)