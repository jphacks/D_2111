# Generated by Django 3.2.7 on 2021-10-25 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectpost', '0012_alter_bookmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readbooksmodel',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectpost.usermodel'),
        ),
    ]
