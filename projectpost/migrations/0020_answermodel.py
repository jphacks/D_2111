# Generated by Django 3.2.7 on 2021-10-29 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectpost', '0019_auto_20211029_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='answerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectpost.usermodel')),
                ('response_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectpost.questionmodel')),
            ],
        ),
    ]
