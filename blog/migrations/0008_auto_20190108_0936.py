# Generated by Django 2.1.5 on 2019-01-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='200', null=True, upload_to='', width_field='100'),
        ),
    ]
