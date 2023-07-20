from django.db import models

class Student(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField()
    subject=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.fname