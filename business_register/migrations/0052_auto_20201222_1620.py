# Generated by Django 3.0.7 on 2020-12-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0051_auto_20201214_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companylinkwithpep',
            name='category',
            field=models.CharField(blank=True, choices=[('bank_customer', 'Клієнт банку'), ('owner', 'Власник'), ('by_position', 'За позицією'), ('manager', 'Керівник'), ('other', 'Інше')], default=None, max_length=15, null=True, verbose_name='категорія'),
        ),
    ]
