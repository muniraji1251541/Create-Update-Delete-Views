from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=50)
    principal=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.name