# Generated by Django 3.2.7 on 2021-10-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20211028_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name_user',
            field=models.CharField(default='', max_length=256),
        ),
    ]
