# Generated by Django 2.1.1 on 2018-09-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
