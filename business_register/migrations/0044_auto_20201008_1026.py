# Generated by Django 3.0.7 on 2020-10-08 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0043_relatedpersonlinkwithpep'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedPersonsLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('person_relationship_type', models.CharField(max_length=90, null=True, verbose_name="тип зв'язку першої особи із іншою")),
                ('other_person_relationship_type', models.CharField(max_length=90, null=True, verbose_name="тип зв'язку іншої особи із першою")),
                ('start_date', models.CharField(max_length=12, null=True, verbose_name="дата виникнення зв'язку")),
                ('confirmation_date', models.CharField(max_length=12, null=True, verbose_name="дата підтвердження зв'язку")),
                ('end_date', models.CharField(max_length=12, null=True, verbose_name="дата припинення зв'язку")),
                ('other_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_related_persons', to='business_register.Pep', verbose_name="інша пов'язана особа")),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='business_register.Pep', verbose_name="пов'язана особа")),
            ],
            options={
                'verbose_name': "пов'язана з публічним діячем особа",
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='relatedpersonlinkwithpep',
            name='pep',
        ),
        migrations.RemoveField(
            model_name='relatedpersonlinkwithpep',
            name='related_person',
        ),
        migrations.DeleteModel(
            name='PepRelatedPerson',
        ),
        migrations.DeleteModel(
            name='RelatedPersonLinkWithPep',
        ),
        migrations.AddField(
            model_name='pep',
            name='related_persons',
            field=models.ManyToManyField(related_name='_pep_related_persons_+', through='business_register.RelatedPersonsLink', to='business_register.Pep'),
        ),
    ]
