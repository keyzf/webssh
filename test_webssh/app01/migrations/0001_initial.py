# Generated by Django 2.2.3 on 2019-09-23 08:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogCommandResult',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('login_as_user', models.CharField(max_length=45)),
                ('login_org_user', models.CharField(max_length=45)),
                ('login_org_name', models.CharField(max_length=45)),
                ('cmd_content', models.TextField(null=True)),
                ('login_time', models.DateTimeField(auto_now_add=True)),
                ('recode_time', models.DateTimeField()),
                ('logout_time', models.DateTimeField(null=True)),
            ],
            options={
                'managed': True,
            },
        ),
    ]