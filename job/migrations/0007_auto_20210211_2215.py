# Generated by Django 3.1.6 on 2021-02-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20210211_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='upload_cv',
            field=models.FileField(upload_to='apply/'),
        ),
    ]