from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=122)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Contact'

    def __str__(self):
        return self.name + self.email