from rest_framework import serializers
from django.contrib.auth.models import User
from ClientApp.models import Clients,Product,Bills,Bills_Products

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username', 'email','first_name', 'last_name')

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clients
        fields=('idClient', 'firstNameClient', 'lastNameClient', 'documentClient', 'emailClient')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('idProduct', 'NameProduct', 'descripcionProduct', 'attributeProduct')

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bills
        fields=('idBill', 'NameCompany', 'nitBill', 'dateBill', 'codeBill', 'clienteId')

class Bills_ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bills_Products
        fields=('idBills_Products', 'clienteIdBP', 'productIdBP')