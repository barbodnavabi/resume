# Generated by Django 3.1.6 on 2021-02-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210204_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='how',
            field=models.CharField(blank=True, max_length=300, verbose_name='کجا یا چگونه'),
        ),
    ]
