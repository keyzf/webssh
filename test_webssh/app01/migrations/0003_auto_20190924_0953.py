# Generated by Django 2.2.3 on 2019-09-24 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190923_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logcommandresult',
            name='recode_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]