from django.contrib import admin

# Register your models here.
from .models import (
    Company,
    Medicine,
    MedicalDetails,
    Employee,
    EmployeeSalary,
    EmployeeBank,
    Customer,
    Bill,
    BillDetails,
    CustomerRequest, CompanyAccount, CompanyBank
)

admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(MedicalDetails)
admin.site.register(Employee)
admin.site.register(EmployeeBank)
admin.site.register(EmployeeSalary)
admin.site.register(Bill)
admin.site.register(BillDetails)
admin.site.register(Customer)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
