# Generated by Django 3.0.5 on 2020-05-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarpvAPP', '0003_auto_20200502_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_user',
            name='clientID',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
