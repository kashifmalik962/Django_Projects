from django.db import models

# Create Company models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT','IT'),
                                                     ('Non IT', 'Non IT'), 
                                                     ('Mobiles Phone', 'Mobiles phone')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Create Employee models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    about = models.TextField(max_length=100)
    position = models.CharField(max_length=100, choices=(
        ('Manager','Manager'),
        ('Software developer','Software developer'),
        ('Project Leader','Project Leader')
    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)