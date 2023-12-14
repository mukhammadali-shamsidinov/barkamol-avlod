# Generated by Django 5.0 on 2023-12-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='auth_status',
            field=models.CharField(choices=[('ordernary', 'ordernary'), ('manager', 'manager'), ('admin', 'admin')], default=1),
            preserve_default=False,
        ),
    ]
