# Generated by Django 2.2.4 on 2019-08-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190815_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='горячий продукт?'),
        ),
    ]
