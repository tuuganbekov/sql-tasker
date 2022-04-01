from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    manufacturer = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name
