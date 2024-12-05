from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=150)
    license_num = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    description = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    medical_type = models.CharField(max_length=255)
    buy_price = models.CharField(max_length=255)
    sell_price = models.CharField(max_length=255)
    c_gst = models.CharField(max_length=255)
    s_gst = models.CharField(max_length=255)
    batch_no = models.CharField(max_length=50)
    shelf_no = models.CharField(max_length=50)
    exp_date = models.DateField()
    mfg_date = models.DateField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    in_stock_total = models.IntegerField()
    qty_in_strip = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)


class MedicalDetails(models.Model):
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=150)
    salt_qty = models.CharField(max_length=10)
    salt_qty_type = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):
    name = models.CharField(max_length=150)
    joining_date = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

class EmployeeSalary(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_day = models.DateField()
    salary_amount = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

class Bill(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

class BillDetails(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    qty = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

class CustomerRequest(models.Model):
    customer_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    medical_details = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    request_date = models.DateTimeField(auto_now_add=True)

TRANSACTION_TYPE = (
    ('Credit', 'credit'),
    ('Debit', 'debit'),
)
class CompanyAccount(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=50)
    transaction_amount = models.CharField(max_length=200)
    transaction_date = models.DateField()
    payment_method = models.CharField(max_length=100)

class CompanyBank(models.Model):
    bank_account_no = models.CharField(max_length=100)
    ifsc_no = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

class EmployeeBank(models.Model):
    bank_account_no = models.CharField(max_length=100)
    ifsc_no = models.CharField(max_length=100)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)







