# Generated by Django 3.0.7 on 2020-07-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0016_auto_20200626_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='founderfull',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='historicalfounderfull',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
