# Generated by Django 4.2.4 on 2023-08-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='post', verbose_name='썸네일'),
        ),
    ]
