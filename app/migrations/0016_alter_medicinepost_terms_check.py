# Generated by Django 3.2.5 on 2021-11-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_medicinepost_terms_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='terms_check',
            field=models.BooleanField(null=True),
        ),
    ]
