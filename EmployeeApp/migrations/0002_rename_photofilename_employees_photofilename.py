# Generated by Django 4.0.2 on 2022-02-18 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='PhotoFilename',
            new_name='PhotoFileName',
        ),
    ]