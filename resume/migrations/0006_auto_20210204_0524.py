# Generated by Django 3.1.6 on 2021-02-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_projects_forwho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, upload_to='projects', verbose_name='عکس پروژه'),
        ),
    ]