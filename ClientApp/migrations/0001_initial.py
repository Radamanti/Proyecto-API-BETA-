# Generated by Django 4.0 on 2021-12-20 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('idClient', models.AutoField(primary_key=True, serialize=False)),
                ('firstNameClient', models.CharField(max_length=500)),
                ('lastNameClient', models.CharField(max_length=500)),
                ('documentClient', models.IntegerField()),
                ('emailClient', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('idProduct', models.AutoField(primary_key=True, serialize=False)),
                ('NameProduct', models.CharField(max_length=500)),
                ('descripcionProduct', models.CharField(max_length=500)),
                ('attributeProduct', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bills_Products',
            fields=[
                ('idBills_Products', models.AutoField(primary_key=True, serialize=False)),
                ('clienteIdBP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClientApp.clients')),
                ('productIdBP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClientApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('idBill', models.AutoField(primary_key=True, serialize=False)),
                ('NameCompany', models.CharField(max_length=500)),
                ('nitBill', models.IntegerField()),
                ('dateBill', models.DateField()),
                ('codeBill', models.IntegerField()),
                ('clienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClientApp.clients')),
            ],
        ),
    ]
