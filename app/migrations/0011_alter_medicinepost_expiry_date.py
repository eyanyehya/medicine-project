# Generated by Django 3.2.5 on 2021-11-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_medicinepost_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]
