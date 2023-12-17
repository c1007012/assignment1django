# Generated by Django 4.2.7 on 2023-12-15 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleRegistrationSystem', '0003_module_courses_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('credit', models.PositiveIntegerField()),
                ('description', models.TextField(default='No description provided.')),
            ],
        ),
    ]
