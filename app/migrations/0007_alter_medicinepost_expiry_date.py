# Generated by Django 3.2.5 on 2021-11-01 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_medicinepost_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='expiry_date',
            field=models.CharField(blank=True, default='NA', max_length=200, null=True),
        ),
    ]
