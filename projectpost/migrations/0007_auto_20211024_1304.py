# Generated by Django 3.2.7 on 2021-10-24 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectpost', '0006_rename_images_usermodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junresmodels',
            name='junres',
            field=models.CharField(default='django llvm agax', max_length=200),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(default='media/ともや.JPG', upload_to=''),
        ),
    ]
