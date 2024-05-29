from django.db import models

# Create your models here.
class registerModel(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name