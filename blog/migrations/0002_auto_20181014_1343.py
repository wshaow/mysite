# Generated by Django 2.0.7 on 2018-10-14 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtype',
            name='type_name',
            field=models.CharField(default='git', max_length=15),
        ),
    ]
