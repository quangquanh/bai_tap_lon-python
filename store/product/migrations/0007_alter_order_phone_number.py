# Generated by Django 3.2.7 on 2021-10-28 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20211028_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
