# Generated by Django 4.2.7 on 2023-12-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleRegistrationSystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='No description provided.'),
        ),
    ]