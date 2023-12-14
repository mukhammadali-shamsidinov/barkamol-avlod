# Generated by Django 5.0 on 2023-12-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_auth_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='auth_status',
            field=models.CharField(choices=[('ordernary', 'ordernary'), ('manager', 'manager'), ('admin', 'admin')], default='ordernary'),
        ),
    ]
