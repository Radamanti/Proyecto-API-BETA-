from django.db import models

# Create your models here.

class Clients(models.Model):
    idClient = models.AutoField(primary_key=True)
    firstNameClient = models.CharField(max_length=500)
    lastNameClient = models.CharField(max_length=500)
    documentClient = models.IntegerField(null=False)
    emailClient = models.EmailField()

class Product(models.Model):
    idProduct = models.AutoField(primary_key=True)
    NameProduct = models.CharField(max_length=500)
    descripcionProduct = models.CharField(max_length=500)
    attributeProduct = models.IntegerField(null=False)

class Bills(models.Model):
    idBill = models.AutoField(primary_key=True)
    NameCompany = models.CharField(max_length=500)
    nitBill = models.IntegerField()
    dateBill = models.DateField()
    codeBill = models.IntegerField(null=False)
    clienteId = models.ForeignKey(Clients, on_delete=models.CASCADE)

class Bills_Products(models.Model):
    idBills_Products = models.AutoField(primary_key=True)
    clienteIdBP = models.ForeignKey(Clients, on_delete=models.CASCADE)
    productIdBP = models.ForeignKey(Product, on_delete=models.CASCADE)

class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20, null=False)
    Token = models.IntegerField()
    email = models.EmailField(null = False)