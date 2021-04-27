from django.db import models

# Create your models here.
class profiledata(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email

class comments(models.Model):
    person_name = models.CharField(max_length=30)
    person_message = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.person_name 